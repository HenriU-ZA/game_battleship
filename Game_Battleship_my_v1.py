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


def valid_int(minv, maxv,
              question):  # function will check that input is valid.
	try:
		isint = int(input(question))
		if isint < minv or isint > maxv:
			print("You can only chose between %d and %d" % (minv, maxv))
			isint = valid_int(minv, maxv, question)
	except ValueError:
		print("You have to chose between %d and %d" % (minv, maxv))
		isint = valid_int(minv, maxv, question)
	return isint


build_board(board_size)  # build the board.
bot_row = random_choice(board)  # computer choose row
bot_col = random_choice(board)  # computer chose col
user_row = valid_int(0, len(board) - 1, "Please pick a row: ")
user_col = valid_int(0, len(board) - 1, "Please pick a col: ")
print_board(board)
print(bot_row, bot_col)

#need to write function to play game...
# user will get board size guesses.. ie, bigger board = more choices.
# write a menu to make selections. ie board size. replay. exit...
# improve board display.
