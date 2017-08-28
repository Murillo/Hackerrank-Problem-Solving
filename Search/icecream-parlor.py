# Ice Cream Parlor
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/icecream-parlor/problem

from itertools import combinations

t = int(input().strip())
for i in range(t):
    m = int(input().strip())
    n = int(input().strip())
    li = [int(flavor) for flavor in input().strip().split(' ')]
    flavors_combinations = combinations(li, 2)

    for flavors in flavors_combinations:
        if flavors[0] + flavors[1] == m:
            first_val = li.index(flavors[0])
            second_val = li.index(flavors[1], first_val + 1)
            print ("{} {}".format(first_val + 1, second_val + 1))
            break