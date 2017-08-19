# The Coin Change Problem
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/coin-change/problem

# Não existe limite para a quantidade de caracteres
# Saber se o total é par ou impar

def getWays(n, c):
    # Complete this function
    return 0

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
print (getWays(n, c))
