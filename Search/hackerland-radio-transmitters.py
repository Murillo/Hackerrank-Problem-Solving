# Hackerland Radio Transmitters
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

n,k = [int(points) for points in input().strip().split(' ')]
x   = sorted([int(x_temp) for x_temp in input().strip().split(' ')])
count_transmitters = 0

i = 0
while (i < n):
    count_transmitters += 1
    val = x[i] + k
    while (i < n and x[i] <= val):
        i += 1
    i -= 1
    val = x[i] + k
    while (i < n and x[i] <= val):
        i += 1

print (count_transmitters)