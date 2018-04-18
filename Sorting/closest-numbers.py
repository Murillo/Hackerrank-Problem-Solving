# Closest Numbers
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/closest-numbers/problem
# Time complexity: O(n log n)

def closestNumbers(arr):
	pairs = []
	for i in range(len(arr)):
		if i < len(arr) - 1:
			pairs.append([[arr[i], arr[i + 1]],arr[i + 1] - arr[i] ])
			
	minDiff = min([i[1] for i in pairs])
	selected = [i[0] for i in pairs if i[1] == minDiff]
	result = []
	for item in selected:
		result.append(item[0])
		result.append(item[1])
	return result

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
print (" ".join(map(str, closestNumbers(sorted(arr)))))