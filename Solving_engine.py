grid = [[0,5,2,0,0,6,0,0,0],
        [1,6,0,9,0,0,0,0,4],
        [0,4,9,8,0,3,6,2,0],
        [4,0,0,0,0,0,8,0,0],
        [0,8,3,2,0,1,5,9,0],
        [0,0,1,0,0,0,0,0,2],
        [0,9,7,3,0,5,2,4,0],
        [2,0,0,0,0,9,0,5,6],
        [0,0,0,1,0,0,9,7,0]]

def validity(grid,row,col,x):
    counter = 0
    if x not in grid[row]:
        counter+=1
    if x not in [grid[i][col] for i in range(9)]:
        counter+=1
    if x not in [grid[i][j] for i in range(row//3*3, row//3*3+3) for j in range(col//3*3, col//3*3+3)]:
        counter+=1
    if counter == 3:
        return True
    else:   
        return False
    
def solve(grid):

    find = find_empty(grid)
    if not find:
        return True
    else:
        row,col = find

    for x in range(1,10):
        if validity(grid,row,col,x) == True:
            grid[row][col] = x

            if solve(grid):
                return True
            
            grid[row][col] = 0

    return False

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
    return None

print(solve(grid))
for i in grid:
    print(i)
