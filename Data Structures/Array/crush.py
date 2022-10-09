# Problem: Array Manipulation
# Url: https://www.hackerrank.com/challenges/crush/problem
# Level: Hard
# Developer: Murillo Grübler

###################################################
def arrayManipulation(n, queries):
    arr = [0] * n

    for i in range(len(queries)):
        arr[queries[i][0] - 1] += queries[i][2]
        if queries[i][1] <= n-1:
            arr[queries[i][1]] -= queries[i][2]

    count = 0
    max_val = 0
    for item in arr:
        count += item
        max_val = max(max_val, count)

    return max_val
###################################################

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print (str(result) + '\n')