from itertools import product
log = [['a', 'b'], [1, 2], ['가', '나']]
for case in product(log[0], log[1], log[2]):
    print(case)