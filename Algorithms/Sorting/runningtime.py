# Running Time of Algorithms
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/runningtime/problem

n = int(input().strip())
arr = [int(ar) for ar in input().strip().split(' ')]

count = 0
for i in range(len(arr)):
    k = i
    key = arr[i]
    while k > 0 and key < arr[k - 1]:
        arr[k] = arr[k - 1]
        k -= 1
        count += 1
    arr[k] = key

print (count)