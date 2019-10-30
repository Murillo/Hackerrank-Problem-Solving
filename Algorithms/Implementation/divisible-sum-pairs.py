# Divisible Sum Pairs
# Developer: Murillo Grubler

def divisibleSumPairs(n, k, ar):
    total = 0
    for i in range(n):
        for j in range(n):
            if i < j and ((ar[i] + ar[j]) % k) == 0:
                total += 1
    return total

n, k = [int(numbers) for numbers in input().strip().split(' ')]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)