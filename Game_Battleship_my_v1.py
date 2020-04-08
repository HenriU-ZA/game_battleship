# An update on the previous battleship GAME
# Update log 
# Increased board size and added indexes 
# Changed input selection to a Letter/Number value, and check for validity
# Added bot ships :frigate = 2, submarine = 3, destroyer = 3, battleship = 4, carrier = 5
# Added a board that will be hidden with the bot ships


# Imports to allow use of external methods
from string import ascii_uppercase
from random import randint  

# Create some variables for use later on
# Create an emoty game board.
board = []
bot_ship_board = []
# Setting up the ships for the BOT: 
bot_frigate = {
    "name" : "Frigate", 
    "locationxy" : [],
    "hitpoint" : 2}
bot_submarine = {
    "name" : "Submarine", 
    "locationxy" : [],
    "hitpoint" : 3}
bot_destroyer = {
    "name" : "Destroyer", 
    "locationxy" : [],
    "hitpoint" : 3}
bot_battleship = {
    "name" : "Battleship", 
    "locationxy" : [],
    "hitpoint" : 4}
bot_carrier = {
    "name" : "Carrier", 
    "locationxy" : [],
    "hitpoint" : 5}
bot_ships = [bot_carrier, bot_battleship, bot_destroyer, bot_submarine, bot_frigate]
# Set a value to the size of the board
board_size = 12
# Bring the ascii characters into a variable and changing the variable to the letters we want to use.
upper_alph_letter = ascii_uppercase
upper_alph_letter = " " + upper_alph_letter[0:10] + " "

# A Function to build the game board. 
def build_board(board_size, board):
	for _ in range(board_size):
		board.append(["O"] * board_size)

# Add the col and row indexes to the board.
def index_board(upper_alph_letter, board_size, board):
    for i in range(0, len(upper_alph_letter)):
        board[0][i] = upper_alph_letter[i]
        board[11][i] = upper_alph_letter[i]
    for i in range(0, board_size):
        mark = str(i)
        if i < 10:
            mark = " " + mark
        if i == 0 or i == 11:
            mark = "  "
        board[i][0] = mark
        if i < 10 and i > 0:
            mark = str(i)
        board[i][11] = mark

# Update the board with the arguements provided.
def update_board(row, col, mark, board):
	board[row][col] = mark

# Use XY coordinates and update board
def update_board_xy(board, xy, mark):
    # Split xy into 2, a letter aand a number. 
    loc_col = str(xy[0].upper())
    loc_row = int(xy[1:])
    # Get int value for col
    for num in range(1, len(board)-1):
        if loc_col == board[0][num]:
            loc_col = int(num)
    update_board(loc_row, loc_col, mark, board)

# Show the board in its current state.
def print_board(board):  
	for i in range(len(board)):
		print(" ".join(board[i]))

# Build the bot ships
def build_ships(board, bot_ships):
    for ship in bot_ships:
        good = 'n'
        while good == 'n':
            good = 'y'
            xy_loc = random_empty_xy(board)
            bot_row = xy_loc[0]
            bot_col = xy_loc[1]
            row_list = [bot_row]
            col_list = [bot_col]
            #Find and check additional locations. only if all locations check out, can we write to the board and dictionary
            row_col = randint(1,2)
            if row_col == 1 and bot_row > 5:
                #print ('We will be going in rows smaller')
                for i in range(1,ship['hitpoint']):
                    if board[bot_row-i][bot_col] != 'O':
                        good = 'n'
                    else:
                        row_list.append(bot_row - i)
                        col_list.append(bot_col)
            elif row_col == 1 and bot_row < 6:
                #print ('We will be going in rows larger')
                for i in range(1,ship['hitpoint']):
                    if board[bot_row+i][bot_col] != 'O':
                        good = 'n'
                    else:
                        row_list.append(bot_row + i)
                        col_list.append(bot_col)

            elif row_col == 2 and bot_col > 5:
                #print ('We will be going in cols Smaller')
                for i in range(1,ship['hitpoint']):
                    if board[bot_row][bot_col-i] != 'O':
                        good = 'n'
                    else:
                        row_list.append(bot_row)
                        col_list.append(bot_col - i)
            elif row_col == 2 and bot_col < 6:
                #print ('We will be going in cols larger')
                for i in range(1,ship['hitpoint']):
                    if board[bot_row][bot_col+i] != 'O':
                        good = 'n'
                    else:
                        row_list.append(bot_row)
                        col_list.append(bot_col + i)

            for i in range(len(col_list)):
                row_2c = row_list[i]
                col_2c = col_list[i]
                xy = convert_to_xy(row_2c, col_2c, upper_alph_letter)
                update_board_xy(board, xy, ship['name'][0])
                ship['locationxy'].append(xy)
        #print (ship['locationxy'])  #debug

# Convert row & col values to xy coordinates
def convert_to_xy(bot_row, bot_col, upper_alph_letter):
    x_val = upper_alph_letter[bot_col]
    xy_loc = x_val + str(bot_row)
    return xy_loc

# Find an empty spot, and return its location
def random_empty_xy(board):
    xy_loc = []
    bot_row = random_choice(board)
    bot_col = random_choice(board)
    if board[bot_row][bot_col] == "O":
        xy_loc = [bot_row, bot_col]
    else:
        xy_loc = random_empty_xy(board)
    return xy_loc

# Generates a random int, in range of the playable board.
def random_choice(board): 
	return randint(1, len(board) - 1)

# Checks if an input is an int and whether its in a specified range.
def valid_int(minv, maxv, question): 
	try:
		isint = int(input(question))
		if isint < minv or isint > maxv:
			print("You can only chose between %d and %d" % (minv, maxv))
			isint = valid_int(minv, maxv, question)
	except ValueError:
		print("You have to chose between %d and %d" % (minv, maxv))
		isint = valid_int(minv, maxv, question)
	return isint

# Pick coordinates and see if the location is valid
def valid_location(board, question):
    location_valid = input(question)
    loc_col = str(location_valid[0].upper())
    loc_row = str(location_valid[1:])
    if len(loc_row) == 1:
        loc_row = " " + loc_row
    # Set a pass command
    valid_r = "n"
    valid_c = "n"
    for i in range(1, len(board) - 1):
        if loc_col == board[0][i]:
            valid_c = "y"
        if loc_row == board[i][0]:
            valid_r = "y"
    # Set what to do if the commands has passed or failed.
    # Both need to pass in ordder to pass, but only one has to fail in order to fail.        
    if valid_r == "y" and valid_c == "y":
        # If we pass, what to do:
        location_valid = location_valid
    elif valid_r =="n" or valid_c == "n":
        # If we fail we need to try again. 
        print("You have selected invalid coordinates. You need to use the format A1, C3... ")
        location_valid = valid_location(board, "Chose your coordinates: ")
    return location_valid
    



# Plays a round of the game.
def play_round(board, bot_row, bot_col):
    hit = len(board) - 2
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

# Start game by building the board. 
build_board(board_size, board)
index_board(upper_alph_letter, board_size, board)
# Build the computers board, where we can store its ships.
build_board(board_size, bot_ship_board)
index_board(upper_alph_letter, board_size, bot_ship_board)
#print_board(board)
build_ships(bot_ship_board, bot_ships)
print_board(bot_ship_board)

# Mark's H hit, X miss, F frigate, S submarine, D destroyer, B battleship, C carrier. 
# write a menu to make selections.  play vith diff lev, easy, med, hard, superhard exit...
# allow multi player, ie player vs bot, with ships on both ends.
# on multiplayer,  2 boards should be next to one another... choices and my ships
# additional invisible boards for bot ships. and tries.
# on multiplayer game will end when all of one teams ships is sunk.
