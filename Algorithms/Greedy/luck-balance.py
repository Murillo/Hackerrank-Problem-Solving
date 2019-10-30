# Luck Balance
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/luck-balance/problem

n, k =  [int(val) for val in input().strip().split(' ')]
luck = 0
imp_values = []
for i in range(n):
    L, T =  [int(val) for val in input().strip().split(' ')]
    if T == 0:
        luck += L
    else:
        imp_values.append(L) 
imp_values.sort(key=int)
for i in range(k):
    if len(imp_values) > 0:
        luck += imp_values.pop()
print (luck - sum(imp_values))