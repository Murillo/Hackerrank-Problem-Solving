# Hackerland Radio Transmitters
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

# n,k = [int(points) for points in input().strip().split(' ')]
# x   = sorted([int(x_temp) for x_temp in input().strip().split(' ')])
n, k = 8, 2
x = [7, 2, 4, 6, 5, 9, 12, 11]
area_k = (k * 2) + 1
count_area = 1
radios = 0

for i in range(min(x), max(x) + 1):
    print (count_area)
    if count_area == int(area_k / 2):
        radios += 1
        print ("count radio {} na casa {}".format(count_area, i))
    elif ((max(x) - i) / area_k) < 1:
        radios += 1
        print ("count radio {} na casa {}".format(count_area, i))
        break
    elif count_area == area_k:
        count_area = 0
    count_area += 1
print (radios)