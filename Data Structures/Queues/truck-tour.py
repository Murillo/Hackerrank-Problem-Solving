# Truck Tour
# Developer: Murillo Grübler
# https://www.hackerrank.com/challenges/truck-tour/problem

# Time complexity: O(n)
# Space complexity: O(1)
def truckTour(petrolpumps):
    start_position = 0
    fuel = 0
    for i in range(len(petrolpumps)):
        fuel += petrolpumps[i][0] - petrolpumps[i][1]
        if fuel < 0:
            start_position = i + 1
            fuel = 0
    return start_position

if __name__ == '__main__':
    n = int(input().strip())
    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)
    print (str(result))
