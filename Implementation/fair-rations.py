# Fair Rations
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/fair-rations/problem

import os

def fairRations(B):
    if sum(B) % 2 == 0:
        total = 0
        for i in range(len(B)):
            if B[i] % 2 != 0:
                B[i] += 1
                B[i+1] += 1
                total += 1
        return total * 2
    else:
        return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    N = int(input())
    B = list(map(int, input().rstrip().split()))
    result = fairRations(B)
    print (str(result) + '\n')
    # fptr.write(str(result) + '\n')
    # fptr.close()



