# The Time in Words
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/the-time-in-words
# Time Complexity = O(1)

def taumBday(b, w, x, y, z):
    # Complete this function
    return 0

t = int(input().strip())
for a0 in range(t):
    b, w = input().strip().split(' ')
    b, w = [int(b), int(w)]
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    result = taumBday(b, w, x, y, z)
    print(result)