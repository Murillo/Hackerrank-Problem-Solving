# Connected Cells in a Grid
# Developer: Murillo Grubler
# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

def count_largest_region(grid, row, cell):
    print (grid)
    start_row = 0
    start_cell = 0
    rows = len(grid)
    cells = len(grid[0])

    print (rows)
    print (cells)

    # if cell > 0 and cell <= cells:
    #     start_cell = cell - 1

    return 0

def connected_cells(grid):
    size = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total = count_largest_region(grid, i, j)
            size = total if total > size else size
    return 0

grid = []
rows = int(input().strip())
cells = int(input().strip())

for i in range(rows):
    row = ([int(cell) for cell in input().strip().split(' ')])
    grid.append(row)

print(connected_cells(grid))