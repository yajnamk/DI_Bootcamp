import time
board = { 1 : ' ', 2 : ' ', 3: ' ',
   4 : ' ', 5 : ' ', 6 : ' ', 
   7 : ' ', 8 : ' ', 9 : ' '}

# Initialize variables
count = 0			# counter to track number of filled slots
winner = False		        # boolean to check if anyone won
play = True			# boolen to check if the game should continue
tie = False			# boolean to check if there is a tie
curr_player = ''		# variable to store current player identifier
player_details = []		# list to store player identifier and marker

while play:
	["execute game code"]

def printBoard():
  for i in board:
   print( i, ':', board[i], ' ', end="")
   if i%3 == 0:
    print()

def print_board():
    """Function to print the board"""
    for i in board:
        print( i, ':', board[i], ' ', end='')
        if i%3 == 0:
            print()


def win_game(marker, player_id):
    """Function to check for winning combination"""
    if board[1] == marker and board[2] == marker and board[3] == marker or \
    board[4] == marker and board[5] == marker and board[6] == marker or \
    board[7] == marker and board[8] == marker and board[9] == marker or \
    board[1] == marker and board[4] == marker and board[7] == marker or \
    board[2] == marker and board[5] == marker and board[8] == marker or \
    board[3] == marker and board[6] == marker and board[9] == marker or \
    board[1] == marker and board[5] == marker and board[9] == marker or \
    board[3] == marker and board[5] == marker and board[7] == marker:

        print_board()
        time.sleep(1)
        print("Player", player_id, "wins!")
        return True

    else:
        return False