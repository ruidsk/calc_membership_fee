import sys
from typing import Union
from config import *


class OrganisationUnitConfig:
    def __init__(self, has_fixed_membership_fee: bool, fixed_membership_fee_amount: int):
        self.has_fixed_membership_fee = has_fixed_membership_fee
        self.fixed_membership_fee_amount = fixed_membership_fee_amount

class OrganisationUnit:
    def __init__(self, name: str, config: OrganisationUnitConfig):
        self.name = name
        self.config = config
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def get_root(self):
        node = self
        while node.parent is not None:
            node = node.parent
        return node





def calculate_membership_fee(rent_amount: int, rent_period: str, organisation_unit: OrganisationUnit) -> int:
    if rent_period not in ['week', 'month']:
        raise ValueError('Invalid rent period')

    if rent_period == 'week':
        min_rent_amount = 25 * 100  # 25 per week, converted to pence
        max_rent_amount = 2000 * 100  # 2000 per week, converted to pence
    else:
        min_rent_amount = 110 * 100  # 110 per month, converted to pence
        max_rent_amount = 8660 * 100  # 8660 per month, converted to pence
    
    if rent_amount < min_rent_amount or rent_amount > max_rent_amount:
        raise ValueError(f'Rent amount should be between {min_rent_amount/100} and {max_rent_amount/100}')
    
    membership_fee = rent_amount / 100 * 1.2  # +20% VAT
    if membership_fee < 120 * 1.2:
        membership_fee = 120 * 1.2
    
    if organisation_unit.config:
        if organisation_unit.config.has_fixed_membership_fee:
            membership_fee = organisation_unit.config.fixed_membership_fee_amount / 100   
    elif organisation_unit.parent:
        return calculate_membership_fee(rent_amount, rent_period, organisation_unit.parent)
    
    return int(membership_fee)



def create_organization(organisation_structure, organisation_structure_config):
    
    nodes = {}
    # Create OrganisationUnit objects for each item in the configuration
    for config in organisation_structure_config:
        node = OrganisationUnit(config["name"], OrganisationUnitConfig(config["config"]["has_fixed_membership_fee"], config["config"]["fixed_membership_fee_amount"]) if config["config"] else None)
        nodes[config["name"]] = node
    
    # Connect OrganisationUnit objects based on the input digraph
    for connection in organisation_structure:
        parent_name = connection["name"]
        child_names = connection["connection"]
        for child_name in child_names:
            nodes[parent_name].add_child(nodes[child_name])

            
    # Return the organization structure
    return nodes

organization_tree = create_organization(organisation_structure, organisation_structure_config)


# 3 different types of functions for multiple test options
def test():

    while True:
        try:
            rent_amount = int(input("rent amount (int £):")) *100
            rent_period = str(input("rent period (week/month):"))
            organisation_unit_node = organization_tree[str(input("branch instance of organisation unit:"))]
            membership_fee = calculate_membership_fee(rent_amount, rent_period, organisation_unit_node)
            print(membership_fee) 
        except ValueError:
            print("Please enter a valid input.")



def test_2(rent_amount,rent_period,organisation_unit):
    rent_amount *= 100  #  convert to pence
    organisation_unit_node = organization_tree[organisation_unit]
    membership_fee = calculate_membership_fee(rent_amount, rent_period, organisation_unit_node)
    print(membership_fee) 


def test_3():     
    rent_amount_1 = int(sys.argv[1])
    rent_period_1 = str(sys.argv[2])
    organisation_unit_node_1 = organization_tree[str(sys.argv[3])]
    test_2(rent_amount_1,rent_period_1,organisation_unit_node_1)

