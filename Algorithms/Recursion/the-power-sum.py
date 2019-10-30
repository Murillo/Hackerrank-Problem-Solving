# The Power Sum
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/the-power-sum/problem

import math

def get_power_sum(s, p, n):
    count = s - (n ** p)
    print (count)
    if count == 0:
        return 1
    elif count < 0:
        return 0
    else:
        return get_power_sum(count, p, n + 1) + get_power_sum(s, p, n + 1)

s = int(input().strip())
p = int(input().strip())
n = 1
print (get_power_sum(s, p, n))