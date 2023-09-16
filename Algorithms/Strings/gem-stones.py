# Gemstones
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/gem-stones/problem

# Time complexity: O(n)
# Space complexity: O(n)
def gemstones(arr):
    gems_used = {}
    total_stones = len(arr)

    for i in range(len(arr)):
        gems_used_by_stone = {}
        for j in range(len(arr[i])):
            if arr[i][j] not in gems_used:
                gems_used[arr[i][j]] = gems_used_by_stone[arr[i][j]] = 1
            elif arr[i][j] in gems_used and arr[i][j] not in gems_used_by_stone:
                gems_used[arr[i][j]] += 1
                gems_used_by_stone[arr[i][j]] = 1

    total = 0
    for value in gems_used.values():
        if value == total_stones:
            total += 1
    return total

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr.append(str(input().strip()))
print(gemstones(arr))