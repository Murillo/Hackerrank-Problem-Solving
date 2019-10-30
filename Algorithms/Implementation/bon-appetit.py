# Bon Appétit
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(n, k, b, ar):
    costs = []
    for i in range(len(ar)):
        if i != k:
            costs.append(ar[i])
    total_ana_costs = sum(costs) / 2
    if b == total_ana_costs:
        return "Bon Appetit"
    else:
        return int(b - total_ana_costs)

n, k = list(map(int, input().strip().split(' ')))
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)