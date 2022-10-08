# Problem: Sparse Arrays
# Url: https://www.hackerrank.com/challenges/sparse-arrays/problem
# Level: Medium
# Developer: Murillo Grübler

###################################################
def matchingStrings(stringList, queries):
    dict_queries = {}
    for item in queries:
        dict_queries[item] = 0

    for string in stringList:
        if string in dict_queries:
            dict_queries[string] += 1

    result = []
    for item in queries: 
        result.append(dict_queries[item])

    return result
###################################################

if __name__ == '__main__':
    stringList_count = int(input().strip())
    stringList = []
    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)
    print ('\n'.join(map(str, res)))
    print ('\n')