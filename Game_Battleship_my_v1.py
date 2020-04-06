#######################
# Game of battleship. #
# Originally did the one on codecademy,
# but felt that one was lacking features.
# This is my version.
######################
from random import randint  # to allow us to call a random integer
board = []  # create an empty board

board_size = 5  # this will become a user selection later


def build_board(board_size):  # function to build board.
	for _ in range(board_size):
		board.append(["O"] * board_size)


def print_board(board):  # function to show the board
	for i in range(len(board)):
		print(" ".join(board[i]))


def random_choice(board):  # function will generate int in range
	return randint(0, len(board) - 1)


def update_board(row, col, mark):  # function will update board.
	board[row][col] = mark


def valid_int(minv, maxv, question):  # function will check that input is valid.
	try:
		isint = int(input(question))
		if isint < minv or isint > maxv:
			print("You can only chose between %d and %d" % (minv, maxv))
			isint = valid_int(minv, maxv, question)
	except ValueError:
		print("You have to chose between %d and %d" % (minv, maxv))
		isint = valid_int(minv, maxv, question)
	return isint

def play_round(board, bot_row, bot_col):
    hit = len(board)
    battle_result = "You could not find my ship!"
    while hit > 0:
        print ("You have %d tries left." %(hit))
        user_row = valid_int(0, len(board) - 1, "Please pick a row: ")
        user_col = valid_int(0, len(board) - 1, "Please pick a col: ")
        # See if the user hit the ship
        if user_row == bot_row and user_col == bot_col:
            print ("You hit my ship!")
            battle_result = "You found my ship and are Victorious! "
            hit = hit - 100
        # See if this is a new selection
        elif board[user_row][user_col] == "X":
            print ("You already picked that spot.")
        # If user did not hit, and it is a new selection he missed. 
        else:
            print ("You missed my ship...")
            board[user_row][user_col] = "X"
            print_board(board)
            hit = hit - 1
    else: 
        print ("GAME OVER!", battle_result)
        board[bot_row][bot_col] = "S"
        print_board(board)
    return hit


build_board(board_size)  # build the board.
bot_row = random_choice(board)  # computer choose row
bot_col = random_choice(board)  # computer chose col
print_board(board)
play_count = play_round(board,  bot_row, bot_col)
print("My ship was at row %d and col %d" %(bot_row, bot_col))

# more ships... of different sizes if you hit one, get extra guesses
# 2 boards. 1 for tries, another for ships
# frigate = 2, submarine = 3, destroyer = 3, battleship = 4, carrier = 5
# Mark's H hit, X miss, F frigate, S submarine, D destroyer, B battleship, C carrier. 
# write a menu to make selections.  replay. exit...
# improve board display.
# mark boards with rows 0-9 and cols a-j
# allow multi player, ie player vs bot, with ships on both ends.
# on multiplayer,  2 boards should be next to one another... choices and my ships
# additional invisible boards for bot ships. and tries.
# on multiplayer game will end when all of one teams ships is sunk.
