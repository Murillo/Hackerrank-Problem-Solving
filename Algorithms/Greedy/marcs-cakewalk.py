# Marc's Cakewalk
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/marcs-cakewalk/problem

# Function O(n)
def must_walk(n, arr):
    count = 0
    for i in range(n):
        count = count + (arr[i] * (2 ** i))
    return count
    
n = int(input().strip())
calories = sorted(list(map(int, input().strip().split(' '))), reverse=True)
print (must_walk(n, calories))