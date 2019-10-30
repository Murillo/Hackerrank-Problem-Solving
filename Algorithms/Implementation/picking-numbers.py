# Picking Numbers
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/picking-numbers/problem

def picking_number(n, arr):
    max_combinations = 0
    for i in range(n):
        combination = arr.count(arr[i]) + arr.count(arr[i] + 1)
        if combination > max_combinations: 
            max_combinations = combination
    return max_combinations

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print (picking_number(n, a))