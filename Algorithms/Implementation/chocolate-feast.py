# Chocolate Feast
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/chocolate-feast/problem
# Time Complexity = O(n)

def chocolateFeast(money, cost, free):
    total_money = money
    products = int(money / cost)
    if products >= free:
        change = int(products)
        while change > 0:
            change = change - free
            if change >= 0:
                products += 1
                change += 1
    return products

t = int(input().strip())
for a0 in range(t):
    n, c, m = list(map(int, input().strip().split(' ')))
    print(chocolateFeast(n, c, m))