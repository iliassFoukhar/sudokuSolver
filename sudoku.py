def print_grid(g):
    print("_________________________") 
    for line in range(0,3):
        print("| {} {}".format(grid[line][0],grid[line][1]), end ="")
        print(" {} | {}".format(grid[line][2],grid[line][3]), end ="")        
        print(" {} {} ".format(grid[line][4],grid[line][5]), end ="")        
        print("| {} {}".format(grid[line][6],grid[line][7]), end ="")          
        print(" {} |".format(grid[line][8],grid[line][3]))        
    print("_________________________") 
    for line in range(3,6):
        print("| {} {}".format(grid[line][0],grid[line][1]), end ="")
        print(" {} | {}".format(grid[line][2],grid[line][3]), end ="")        
        print(" {} {} ".format(grid[line][4],grid[line][5]), end ="")        
        print("| {} {}".format(grid[line][6],grid[line][7]), end ="")          
        print(" {} |".format(grid[line][8],grid[line][3]))
    print("_________________________") 
    for line in range(6,9):
        print("| {} {}".format(grid[line][0],grid[line][1]), end ="")
        print(" {} | {}".format(grid[line][2],grid[line][3]), end ="")        
        print(" {} {} ".format(grid[line][4],grid[line][5]), end ="")        
        print("| {} {}".format(grid[line][6],grid[line][7]), end ="")          
        print(" {} |".format(grid[line][8],grid[line][3]))
    print("_________________________") 
    
def add_element(g,x,y,element):
    if element < 10 and element > 0:
        g[y - 1][x - 1] = element
    else:
        print("Impossible to add your element, it should be compromise between 1 and 9")

def remove_element(g,y,x):
    g[y][x] = 0
def empty_grid():
    global grid
    for i in range(0,9):
        for j in range(0,9):
            remove_element(grid,i,j)
def possible_to_add(y,x,element):
    global grid
    for i in range(9):
        if grid[y][i] == element:
            return False
    for i in range(9):
        if grid[i][x] == element:
            return False
    squareX = (x//3)*3
    squareY = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[squareY + i][squareX + j]==element:
                return False
    return True

def grid_is_full(g):
    for i in range(0,9):
        for j in range(0,9):
            if g[i][j]==0:
                return False
    return True

 
def solve():
    global grid 
    if grid_is_full(grid) == True:
        return True
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for i in range(1,10):
                    if possible_to_add(y,x,i):
                        grid[y][x] = i
                        if solve() == True:
                            return True
                        grid[y][x] = 0
                return False

grid = [[9,0,0,0,6,0,0,0,3],
        [1,0,5,0,9,3,2,0,6],
        [0,4,0,0,5,0,0,0,9],
        [8,0,0,0,0,0,4,7,1],
        [0,0,4,8,7,0,0,0,0],
        [7,0,2,6,0,1,0,0,8],
        [2,0,0,0,0,0,0,0,0],
        [5,0,0,0,3,2,0,9,4],
        [0,8,7,0,1,6,3,5,0]]

moreValues = True
while(moreValues == True):
    print("This is the sudoku Solver")
    print("Please remember that zeroes in the grid mean that they are Not available")
    print("tap 0 if you want to add another element to the grid")
    print("tap 1 if you want to remove an element from the grid")
    print("tap 2 if you want to see the grid")
    print("tap 3 if you want a solution")
    print("tap 4 if you want to make the grid empty")
    print("tap 5 if you want to stop")
    choice = int(input(""))
    if choice == 0:
        print("Write the coordinates in this format : x y element")
        entry = [int(x) for x in input().split()]
        add_element(grid,entry[0],entry[1],entry[2])
    elif choice==1:
        print("Write the coordinates in this format : x y")
        entry = [int(x) for x in input().split()]
        remove_element(grid,entry[0], entry[1])
    elif choice ==2:
        print_grid(grid)
    elif choice ==3:
        possibilities = []
        dealt_with_patterns = False
        solve()
    elif choice ==4:
        empty_grid()
    elif choice == 5:
        moreValues = False