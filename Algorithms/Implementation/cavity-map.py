# Cavity Map
# Developer: Murillo Grubler
# Link: https://www.hackerrank.com/challenges/cavity-map/problem
# Time Complexity = O(nˆ2)

def cavityMap(grid):
    total = len(grid)
    for i in range(1, total - 1):
        for j in range(1, total - 1):
            if grid[i][j] > max(grid[i][j-1],grid[i][j+1],grid[i-1][j],grid[i+1][j]):
                grid[i][j] = 'X'

    for i in grid:
        print ("".join(i))
        print ("\n")

if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = list(str(input().strip()))
        grid.append(grid_item)
    cavityMap(grid)