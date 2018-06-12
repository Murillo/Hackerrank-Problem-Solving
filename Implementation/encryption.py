# Encryption
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/encryption/problem
# Time complexity: O(n²)
# Points: 21.00

import os
import math

# Complete the encryption function below.
def encryption(s):
    result = ""
    row = int((math.sqrt(len(s))))
    col = int(math.sqrt(len(s)) + 1)
    for i in range(col):
        j = i
        while j < len(s):
            result += s[j]
            j += col 
        result += " "
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    result = encryption(input())
    #result = encryption("wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny")
    print (result + '\n')
    # fptr.write(result + '\n')
    # fptr.close()
