
# Part of Artificial Intelligence algorithms at https://www.hackerrank.com/

# Meet the bot MarkZoid. 
# It's a cleaning bot whose sensor is a head mounted camera and whose actuators are the wheels beneath it. 
# It's used to clean the floor.

# Complete the function next_move that takes in 3 parameters posr, posc being the co-ordinates of the bot's current position 
# and board which indicates the board state to print the bot's next move.

# The codechecker will keep calling the function next_move till the game is over or you make an invalid move.

# The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move the bot to clean all the dirty cells.


def next_move(posr, posc, board):
    
    
    bot = []
    
    for i in range(len(board)):
        for j in range(len(board)):
            
            if board[posr][posc] == "d":
                return print("CLEAN")
            
            
            if board[i][j] == "b":
                bot = [i, j]

            if i == posr and j > posc:
                if board[i][j] == "d":
                    return print("RIGHT")
            elif i == posr and j < posc:
                if board[i][j] == "d":
                    return print("LEFT")
            elif i > posr:
                if board[i][j] == "d":
                    return print("DOWN")
            elif i < posr:
                if board[i][j] == "d":
                    return print("UP")
    

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)



# python [filename].py