# Gemstones
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/gem-stones/problem

# Time complexity: O(n²)
def gemstones(arr):
    gems_used = []
    tgems = 0
    fstone = arr[0]
    for i in range(len(fstone)):
        if fstone[i] not in gems_used:
            sgams = 1
            for j in range(1, len(arr)):
                if fstone[i] in arr[j]:
                    sgams += 1
            if sgams == len(arr):
                tgems += 1
            gems_used.append(fstone[i])
    return tgems

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr.append(str(input().strip()))
print(gemstones(arr))