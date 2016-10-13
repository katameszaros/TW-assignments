import sys
import os

board = [" ", " ", " ", 
         " ", " ", " ",  
         " ", " ", " "] 

players = [" ", " "]
    
wins = [[0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 4, 8], [2, 4, 6]]  

player2_wins=False


def show_instructions():
    print("Use the numbers to make your move! ")
    print()
    print (1, '|',2, '|',3)
    print ('---------')
    print (4, '|',5, '|',6)
    print ('---------')
    print (7, '|',8, '|',9)


def get_player_names():
    print()
    players[0] = input("Enter name for player1: ")
    players[1] = input("Enter name for player2: ")
    print()
    print(players[1] + " goes first with O, " + players[0] + " is with X")
    print()


def show_game():
    print (board[0], '|',board[1], '|',board[2])
    print ('---------')
    print (board[3], '|',board[4], '|',board[5])
    print ('---------')
    print (board[6], '|',board[7], '|',board[8])
    print()


def new_board():
    global board
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def make_red(char):
    if os.name == 'nt':
        return char
    else:
        return "\u001b[1;31m" + char + "\u001b[0m"


def print_winner(winner_player):
    print(winner_player + make_red(" won") + "!")


def make_winner_combo_red(char,spot1,spot2,spot3):
    #If there is a winner combo, it will make the 3 winner symbol red
    board[spot1] = make_red(char)
    board[spot2] = make_red(char)
    board[spot3] = make_red(char)
    show_game()


def print_and_update_winner(char):
    global player2_wins
    if char == "X":
        print_winner(players[0])
        player2_wins=False
    if char == "O":
        print_winner(players[1])
        player2_wins=True


def play_again():
    again = input("Again(y/n)? ")
    if again == "y":
        new_board()
    elif again == "n":
        print("Until the next time,bye!")
        sys.exit()


def win_combo(char,spot1,spot2,spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        make_winner_combo_red(char,spot1,spot2,spot3)
        print_and_update_winner(char)
        play_again()

def is_there_space():
    board_state = False
    for i in range(len(board)):
        if " " in board[1:9]:
            board_state = True
        else:
            print("It's a tie!")
            print()
            new_board()
            one_round()
    return board_state


def check_winning(char):
     winning = 0
     for x in range(len(wins)):
        win_combo(char ,wins[x][0], wins[x][1], wins[x][2])


def is_valid_move(candidate):
    found_valid_move = False
    if int(candidate)>=0 and int(candidate)<9 :
        found_valid_move = True
    return found_valid_move


def input_safe_digit(message):
    candidate = input(message)
    while not candidate.isdigit():
        print("Enter a valid number!")
        candidate = input(message)
    return candidate


def move(player, symbol, other_symbol, next_player_move):
    while is_there_space() == True:
        move = input_safe_digit(player + " make your move ("+symbol+"): ")
        move = int(move)-1
        if is_valid_move(move) == True:
            if board[int(move)] != symbol and board[int(move)] != other_symbol:
                board[(int(move))] = symbol
                check_winning(symbol)
                clear()
                show_instructions()
                print()
                print()
                show_game()
                next_player_move()
            else:
                print("Taken")
        else:
            print("Invalid move")


def player1_move():
    move(players[0], "X", "O", player2_move)

    
def player2_move():
    move(players[1], "O", "X", player1_move)


def next_move():
    if player2_wins==False:
        player2_move()
        player1_move()
    else:
        player1_move()
        player2_move()        


def one_round():
    show_game()
    next_move()
    check_winning()

def game():
    print("Welcome to TicTacToe!")
    print()
    show_instructions()
    get_player_names()
    one_round()

game()


