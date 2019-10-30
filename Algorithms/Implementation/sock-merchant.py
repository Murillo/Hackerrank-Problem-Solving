# Sock Merchant
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    temp = []
    pairs_socks = 0
    for i in range(n):
        if ar[i] not in temp:
            temp.append(ar[i])
        else:
            pairs_socks += 1
            temp.remove(ar[i])
    return pairs_socks

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
