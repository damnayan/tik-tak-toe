import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPLayer = "X"
winner = None
gameRunning = True


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])



def player_input(board):
    inp = int(input("Enter a number between 1-9 : "))
    if (inp in range(1,10) and board[inp-1] == "-"):
        board[inp-1] = currentPLayer
    elif(inp not in range (1,10)):
        print("Oops Invalid number!")
    else:
        print("Ooops player is already in the position")

def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[1] != "-"):
        winner = board[0]
        return True
    elif(board[3] == board[4] == board[5] and board[4] != "-"):
        winner = board[3]
        return True
    elif(board[6] == board[7] == board[8] and board[7] != "-"):
        winner = board[6]
        return True

def checkRows(board):
    global winner
    if(board[0] == board[3] == board[6] and board[0] != "-"):
        winner = board[0]
        return True
    elif(board[1] == board[4] == board[7] and board[4] != "-"):
        winner = board[1]
        return True
    elif(board[2] == board[5] == board[8] and board[5] != "-"):
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if(board[0] == board[4] == board[8] and board[0] != "-"):
        winner = board[0]
        return True
    elif(board[2] == board[4] == board[6] and board[4] != "-"):
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if ("-" not in board):
        print_board(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    if (checkDiag(board) or checkHorizontal(board) or checkRows(board) == True):
        print(f"The winner is {winner}")
def switch_player():
    global currentPLayer
    if (currentPLayer == "X"):
        currentPLayer = "O"
    else:
        currentPLayer = "X"

def computer(board):
    while currentPLayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()



while gameRunning :
    print_board(board)
    player_input(board)
    checkWin()
    checkTie(board)
    switch_player()
    computer(board)
    checkWin()
    checkTie(board)
    

