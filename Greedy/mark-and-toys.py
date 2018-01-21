# Mark and Toys
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/mark-and-toys/problem
# Time complexity: O(n log n)

def maximumToys(prices, k):
    total = 0
    prices.sort()
    for i in range(len(prices)):
        k = k - prices[i]
        if k >= 0:
            total += 1
        else:
            break 
    return total

n, k = map(int, input().strip().split(' '))
prices = list(map(int, input().strip().split(' ')))
result = maximumToys(prices, k)
print(result)