# Greedy Florist
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/greedy-florist/problem

def getMinimumCost(k, prices):
    prices_sort = sorted(prices, reverse=True)
    i = x = total = 0
    while(i < len(prices_sort)):
        j = 0
        while (j < k n(prices_sort)):
            total += (x + 1) * prices_sort[i]
            i += 1
            j += 1
        x += 1
    return total

n, k = [int(val) for val in input().strip().split(' ')]
c = list(map(int, input().strip().split(' ')))
print(getMinimumCost(k, c))