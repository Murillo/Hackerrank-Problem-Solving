# Luck Balance
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/luck-balance/problem

n, k =  [int(val) for val in input().strip().split(' ')]
luck = 0
no_luck = 0
importants = 0
for i in range(n):
    L, T =  [int(val) for val in input().strip().split(' ')]
    if T == 1:
        importants += 1
    if importants < k:
        luck += L
    else:
        importants = 0
        no_luck += L
    

print (no_luck)
print (luck)
print (luck - no_luck)