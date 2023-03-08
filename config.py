
organisation_structure = [ 
    { "name": "client", "connection": {"division_a", "division_b"} }, 
    { "name": "division_a", "connection": {"area_a", "area_b"} }, 
    { "name": "division_b", "connection": {"area_c", "area_d"} }, 
    { "name": "area_a", "connection": {"branch_a", "branch_b", "branch_c", "branch_d"} }, 
    { "name": "area_b", "connection": {"branch_e", "branch_f", "branch_g", "branch_h"} }, 
    { "name": "area_c", "connection": {"branch_i", "branch_j", "branch_k", "branch_l"} }, 
    { "name": "area_d", "connection": {"branch_m", "branch_n", "branch_o", "branch_p"} }, 
]



organisation_structure_config = [ 
    { "name": "client", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "division_a", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "division_b", "config": {"has_fixed_membership_fee": True, "fixed_membership_fee_amount": 35000} }, { "name": "area_a", "config": {"has_fixed_membership_fee": True, "fixed_membership_fee_amount": 45000} }, { "name": "area_b", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "area_c", "config": {"has_fixed_membership_fee": True, "fixed_membership_fee_amount": 45000} }, { "name": "area_d", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_a", "config": None }, 
    { "name": "branch_b", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_c", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_d", "config": None }, 
    { "name": "branch_e", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_f", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_g", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_h", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_i", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_j", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, 
    { "name": "branch_k", "config": {"has_fixed_membership_fee": True, "fixed_membership_fee_amount": 25000} }, { "name": "branch_l", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_m", "config": None }, 
    { "name": "branch_n", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_o", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} }, { "name": "branch_p", "config": {"has_fixed_membership_fee": False, "fixed_membership_fee_amount": 0} } ]
    


