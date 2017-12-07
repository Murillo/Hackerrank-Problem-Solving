# Greedy Florist
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/greedy-florist/problem

# Import library
import math

def getPrice(prices):
    prices_sort = sorted(prices, reverse=True)
    return sum([(i + 1) * prices_sort[i] for i in range(len(prices_sort))])

def getMinimumCost(n, k, c):
    total_price = 0
    val_group = n / k
    start = 0
    for i in range(k):
        end = math.ceil(val_group) + start if i == 0 else int(val_group) + start 
        total_price += getPrice(c[start:end])
        start += math.ceil(val_group) if i == 0 else int(val_group)   
    return total_price

#n, k = [int(val) for val in input().strip().split(' ')]
#c = list(map(int, input().strip().split(' ')))
#print(getMinimumCost(n, k, c))
print(getMinimumCost(50, 3, [390225, 426456 ,688267 ,800389 ,990107 ,439248 ,240638 ,15991 ,874479 ,568754 ,729927 ,980985 ,132244 ,488186 ,5037 ,721765 ,251885 ,28458 ,23710 ,281490 ,30935 ,897665 ,768945 ,337228 ,533277 ,959855 ,927447 ,941485 ,24242 ,684459 ,312855 ,716170 ,512600 ,608266 ,779912 ,950103 ,211756 ,665028 ,642996 ,262173 ,789020 ,932421 ,390745 ,433434 ,350262 ,463568 ,668809 ,305781 ,815771 ,550800]))
