# Sherlock and Squares
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/sherlock-and-squares/problem

# Libraries
import os

# Function
###################################################
def squares(a, b):
    k = 1
    total = 0
    while k <= int(b/2):
        for i in range(b):
            if i > int(b/2):
                break

            result = k ** 2
            if result >= a and result <= b:
                total += 1
                break
        k += 1
    return total
####################################################

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for q_itr in range(int(input())):
        ab = input().split()
        #result = squares(int(ab[0]), int(ab[1]))
        result = squares(1, 1000)
        print ("Total: " + str(result))
        # fptr.write(str(result) + '\n')
    # fptr.close()
