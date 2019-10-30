# Modified Kaprekar Numbers
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/kaprekar-numbers/problem
# Time complexity: O(n)

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    values = []
    if p == 0 or p == 1:
        values.append(1)
        p = 2

    for i in range(p, q + 1):
        num = str(i**2)
        if len(num) > 1:
            left_number, right_number = int(num[:len(num)//2]), int(num[len(num)//2:])
            if left_number + right_number == i:
               values.append(i)

    if len(values) > 0:
        print (" ".join(map(str, values)))
    else:
        print ("INVALID RANGE")
    

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)
