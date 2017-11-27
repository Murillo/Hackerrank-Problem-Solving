# Service Lane
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/service-lane/problem
# Time complexity of function service_lane: O(n)
# 1: just a bike; 2: a bike and a car; 3: All three vehicles 

def service_lane(width, start, end):
    total_vehicles = 3
    for i in range(len(width)):
        if i >= start and i <= end and width[i] < total_vehicles:
            total_vehicles = width[i]
    return total_vehicles

n,t = list(map(int, input().strip().split(' ')))
width = list(map(int, input().strip().split(' ')))
for a0 in range(t):
    i, j = [int(item) for item in input().strip().split(' ')]
    print(service_lane(width, i, j))
