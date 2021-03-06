

# Part of Artificial Intelligence algorithms at https://www.hackerrank.com/

# Complete the function displayPathtoPrincess which takes in two parameters - the integer N and the character array grid. 
# The grid will be formatted exactly as you see it in the input, 
# so for the sample input the princess is at grid[2][0]. 
# The function shall output moves (LEFT, RIGHT, UP or DOWN) on consecutive lines to rescue/reach the princess. 
# The goal is to reach the princess in as few moves as possible.

# The above sample input is just to help you understand the format. 
# The princess ('p') can be in any one of the four corners.

# Sample Input

# 3
# ---
# -m-
# p--

def displayPathtoPrincess(n,grid):
    princess = []
    board = []
    
    for i in grid:
        board.append(list(map(str, i)))
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == "p":
                prince = [i, j]
                
    if princess == [0, 0]:
        for i in range(n // 2):
            print("UP")
        for i in range(n // 2):
            print("LEFT")
        
    if princess == [0, n - 1]:
        for i in range(n // 2):
            print("UP")
        for i in range(n // 2):
            print("RIGHT")
    if princess == [n - 1, 0]:
        for i in range(n // 2):
            print("DOWN")
        for i in range(n // 2):
            print("LEFT")
    if princess == [n - 1, n - 1]:
        for i in range(n // 2):
            print("DOWN")
        for i in range(n // 2):
            print("RIGHT")

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)


# python [filename].py