grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def transposePrint(grid):
    print()
    y = 0
    while y < len(grid[0]):
        x = 0
        while x < len(grid):
            if x == len(grid) -1:
                print(grid[x][y])
            else:
                print(grid[x][y],end='')
            x += 1
        y += 1
    print()
    
transposePrint(grid)