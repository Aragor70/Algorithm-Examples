
# Part of Artificial Intelligence algorithms at https://www.hackerrank.com/

# Complete the function nextMove which takes in 4 parameters - an integer N, 
# integers r and c indicating the row & column position of the bot and the character array grid "-" 
# and outputs the next move the bot makes to rescue the princess.
# Print the move LEFT, RIGHT, UP or DOWN.

# Sample Input

# 5
# 2 3
# -----
# -----
# p--m-
# -----
# -----

def nextMove(n,r,c,grid):
    
    princess = []
    board = []
    
    for i in grid:
        board.append(list(map(str, i)))
    
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == "p":
                princess = [i, j]
                
                if i == r and j > c:
                    return "RIGHT"
                elif i == r and j < c:
                    return "LEFT"
                elif i > r:
                    return "DOWN"
                elif i < r:
                    return "UP"

    

    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))


# python [filename].py