# Hackerland Radio Transmitters
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

# n,k = [int(points) for points in input().strip().split(' ')]
# x   = sorted([int(x_temp) for x_temp in input().strip().split(' ')])
n, k = 5, 1
x = [1, 2, 3, 4, 5]
area_k = (k * 2) + 1
count_area = 0
radios = 0

for i in range(min(x), max(x) + 1):
    print (i)
    if count_area == int(area_k / 2):
        radios += 1
        print ("radio na casa {}".format(i))
    elif count_area == area_k:
        count_area = 0
        if (max(x) - i) < area_k:
            radios += 1
            print ("radio na casa {}".format(i))

    count_area += 1

print (radios)