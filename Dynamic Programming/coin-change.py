# The Coin Change Problem
# Developer: Murillo Grübler
# Link: https://www.hackerrank.com/challenges/coin-change/problem
# Time complexity: O(n²)

def getWays(arr, m, n):
	table = [1 if i == 0 else 0 for i in range(n + 1)]
	for i in range(m):
		for j in range(1, len(table)):
			result = j - arr[i]
			if result >= 0:
				table[j] = table[result] + table[j]
	return table[len(table)-1]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
arr = list(map(int, input().strip().split(' ')))
print(getWays(arr, m, n))