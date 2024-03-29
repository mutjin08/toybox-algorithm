from itertools import product
arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for case in product(*arr):
    print(case)