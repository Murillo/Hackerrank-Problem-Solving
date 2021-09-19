# Sum vs XOR
# https://www.hackerrank.com/challenges/sum-vs-xor/problem

def sumXor(n):
    if n == 0:
        return 1
    return 1 << f'{n:b}'.count('0')

n = int(input().strip())
result = sumXor(n)
print (result)