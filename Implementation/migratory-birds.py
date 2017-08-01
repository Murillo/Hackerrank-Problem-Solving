# Migratory Birds
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/migratory-birds/problem

def amount(ar):
    types = {}
    for i in range(len(ar)):
        if ar[i] in types:
            types[ar[i]] += 1
        else:
            types[ar[i]] = 1
    return types

def migratoryBirds(ar):
    all_types = amount(ar)
    types = 0
    quantity = 0
    for key, value in all_types.items():
        if value == quantity and types > key:
            types = key
            quantity = value
        elif value > quantity and types != key:
            types = key
            quantity = value
    return types 

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
print(migratoryBirds(ar))