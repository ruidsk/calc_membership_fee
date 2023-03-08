from calc_membership_fee import test_2

test_inputs = [[600, 'week', 'branch_a'],
               [2000, 'month', 'branch_b'],
               [600, 'week', 'branch_c'],
               [4050, 'month', 'branch_d'],
               [5000, 'month', 'branch_e'],
               ]

for test in test_inputs:
    test_2(test[0],test[1],test[2])