# Picking Numbers
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/picking-numbers/problem

from collections import Counter

def picking_number(n, arr):
    numbers = []
    for i in range(n):
        composition = [arr[i]]
        for j in range(n):
            if  i != j and arr[i] - arr[j] <= 1 and arr[i] - arr[j] >= -1:
                composition.append(arr[j])
        if len(composition) > len(numbers):
            numbers = composition

    # print (numbers)
    min_num = numbers.count(min(numbers)) + numbers.count(min(numbers) + 1)
    max_num = numbers.count(max(numbers)) + numbers.count(max(numbers) - 1)
    return min_num if min_num >= max_num else max_num

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print (picking_number(n, a))