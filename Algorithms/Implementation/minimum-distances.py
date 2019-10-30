# Minimum Distances
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/minimum-distances/problem
# Time complexity: O(n²)

def min_distance(ar, total_distance):
    distance = total_distance
    for i in range(len(ar)):
        for j in range(len(ar)):
            if ar[i] == ar[j] and i != j:
                cur_dist = abs(i - j)
                distance = cur_dist if cur_dist < distance else distance
                break
    return distance if distance != total_distance else -1

n = int(input().strip())
ar = [int(A_temp) for A_temp in input().strip().split(' ')]
print (min_distance(ar, n))