# ********
# This file is individualized for NetID huxing.
# ********

# TODO: implement pad(num)
# Return a string representation of num that is always two characters wide.
# If num does not already have two digits, a leading "0" is inserted in front.
# This is called "padding".  For example, pad(12) is "12", and pad(1) is "01".
# You can assume num is either one or two digits long.
def pad(num: int) -> str:
    if num <= 9:
        return "0"+f"{num}"
    else:
        return f"{num}" # replace with your implementation

# TODO: implement pad_all(nums)
# Return a new list whose elements are padded versions of the elements in nums.
# For example, pad_all([12, 1]) should return ["12", "01"].
# Your code should create a new list, and not modify the original list.
# You can assume each element of nums is an int with one or two digits.
def pad_all(nums: list) -> list:
    new_list = []
    for i in range(len(nums)):
        if (nums[i]) < 10 :
            new_list.append("0" + f"{nums[i]}")
        else:
            new_list.append(f"{nums[i]}")
    return new_list# replace with your implementation

# TODO: implement initial_board()
# Return a list of ints representing the initial mancala board at the start of the game.
# The list element at index p should be the number of gems at position p.
def initial_board() -> list:
    return [2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0] # replace with your implementation

# TODO: implement is_not_over(board)
# Return True if the game is not over, and False otherwise.
# If both players have at least one non-empty pit on the board, the game is not over.
# Otherwise, it is over. 
# Your code should not modify the board list.
# The built-in functions "any" and "all" may be useful:
#   https://docs.python.org/3/library/functions.html#all
def is_not_over(board: list) -> bool:
    if board[0] == board[1] ==board[2]==board[3]==board[4]== 0:
        return False
    elif board[6] == board[7] ==board[8]==board[9]==board[10]== 0:
        return False
    else:
        return True
     # replace with your implementation

# TODO: implement valid_moves(player, board)
# Return a list of all positions on the board where the player can pick up gems.
# A position is a valid move if it is one of the player's pits and has 1 or more gems in it.
# For example, if all of player's pits are empty, you should return [].
# The positions in the returned list should be ordered from lowest to highest.
# Your code should not modify the board list.
def valid_moves(player: int, board: list) -> list:
    list = []
    if player == 0:
        for i in range(5):
            if board[i] > 0:
                list.append(i)
    else:
        for i in range(6,11):
            if board[i] > 0:
                list.append(i)
    return list # replace with your implementation

# TODO: implement mancala_of(player)
# Return the numeric position of the given player's mancala.
# Player 0's mancala is on the right and player 1's mancala is on the left.
# You can assume player is either 0 or 1.
def mancala_of(player: int) -> int:
    if player == 0:
        return 5
    if player == 1:
        return 11 # replace with your implementation

# TODO: implement pits_of(player)
# Return a list of numeric positions corresponding to the given player's pits.
# The positions in the list should be ordered from lowest to highest.
# Player 0's pits are on the bottom and player 1's pits are on the top.
# You can assume player is either 0 or 1.
def pits_of(player: int) -> list:
    if player == 0:
        return [0,1,2,3,4]
    if player == 1:
        return [6,7,8,9,10] # replace with your implementation

# TODO: implement player_who_can_do(move)
# Return the player (either 0 or 1) who is allowed to perform the given move.
# The move is allowed if it is the position of one of the player's pits.
# For example, position 2 is one of player 0's pits.
# So player_who_can_do(2) should return 0.
# You can assume that move is a valid position for one of the players.
def player_who_can_do(move: int) -> int:
    if move <=4:
        return 0
    if move >5:
        return 1 # replace with your implementation

# TODO: implement opposite_from(position)
# Return the position of the pit that is opposite from the given position.
# Check the pdf instructions for the definition of "opposite".
def opposite_from(position: int) -> int:
    return (10-position) # replace with your implementation

# TODO: implement play_turn(move, board)
# Return the new game state after the given move is performed on the given board.
# The return value should be a tuple (new_player, new_board).
#   new_player should be an int, 0 or 1, for the player whose turn it is after the move.
#   new_board should be a list representing the new board state after the move.
#
# Parameters:
#   board is a list representing the current state of the game board before the turn is taken.
#   move is an int representing the position where the current player picks up gems.
# You can assume that move is a valid move for the current player who is taking their turn.
# Check the pdf instructions for the detailed rules of taking a turn.
#
# It may be helpful to use several of the functions you implemented above.
# You will also need control flow such as loops and if-statements.
# Lastly, the % (modulo) operator may be useful:
#  (x % y) returns the remainder of x / y
#  from: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
def play_turn(move: int, board: list) -> tuple:
    new_player = 0
    new_board = board
    if new_player == 0:
        for i in range(1,board[move]+1):
            new_board[move] = 0
            board[move+i] += 1
            #if ((board[move]) % 11) < 0:
                #new_player = 1
            if board[5] == 0:
                new_player = 1
    if new_player == 1:
        for i in range(1, board[move]):
            new_board[move] = 0
            board[move + i] += 1
            if board[11] == 1:
                new_player = 1
            else:
                new_player = 0
    return (new_player,board) # replace with your implementation

# TODO: implement clear_pits(board)
# Return a new list representing the game state after clearing the pits from the board.
# When clearing pits, any gems in a player's pits get moved to that player's mancala.
# Check the pdf instructions for more detail about clearing pits.
def clear_pits(board: list) -> list:
    player1 = 0
    player2 = 0
    if is_not_over(board) == False:
        for i in range(6):
            player1 += board[i]
        board[0] = board[1] =board[2]=board[3]=board[4]= 0
        board[5] = player1
        for e in range(6,12):
            player2 += board[e]
        board[6] = board[7] = board[8] = board[9] = board[10] = 0
        board[11] = player2
    return board # replace with your implementation

# TODO: implement is_tied(board)
# Return True if the game is tied in the given board state, False otherwise.
# A game is tied if both players have the same number of gems in their mancalas.
# You can assume all pits have already been cleared on the given board.
def is_tied(board: list) -> bool:
    if board[5] == board[11]:
        return True
    else:
        return False # replace with your implementation

# TODO: implement winner_of(board)
# Return the winning player (either 0 or 1) in the given board state.
# The winner is the player with more gems in their mancala.
# You can assume it is not a tied game, and all pits have already been cleared.
def winner_of(board: list) -> int:
    if board[5] < board[11]:
        return 1
    else:
        return 0 # replace with your implementation

# TODO: implement string_of(board)
# Return a string representation of the given board state for text-based game play.
# The string should have three indented lines of text.
# The first line shows the number of gems in player 1's pits,
# the second line shows the number of gems in each player's mancala,
# and the third line shows the number of gems in player 0's pits.
# The gem numbers should be padded and evenly spaced.
# For example, the string representation of the initial game state is:
# 
#            02 02 02 02 02
#         00                00
#            02 02 02 02 02
# 
# Another example for a different game state with more gems is:
# 
#            12 12 12 12 12
#         00                00
#            02 02 02 02 02
# 
# Excluding the leading comment symbols "# " above, all blank space should match exactly:
#   There are exactly 8 blank spaces before the left (padded) mancala number.
#   There is exactly 1 blank space between each (padded) pit number.
#   The returned string should start and end with new-line characters ("\n")
# The "join" string method may be useful:
#   https://docs.python.org/3/library/stdtypes.html#str.join
# For example, " | ".join(["a", "b", "c"]) returns "a | b | c"
def string_of(board: list) -> str:


    b = ("\n"   +" "+" "+" "+" "+" "+" "+" "+ " "+ " "+ " " +      " "+ f"{pad(board[10])}"+ " "+ f"{pad(board[9])}"+ " "+ f"{pad(board[8])}"+ " "+ f"{pad(board[7])}"+" "+ f"{pad(board[6])}"+"\n" +" "+" "+" "+" "+" "+" "+" "+" " f"{pad(board[11])}" +" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+ f"{pad(board[5])}""\n"+" "+" "+" "+" "+" "+" "+" "+ " "+ " "+ " " +      " "+ f"{pad(board[0])}"+ " "+ f"{pad(board[1])}"+ " "+ f"{pad(board[2])}"+ " "+ f"{pad(board[3])}"+" "+ f"{pad(board[4])}""\n")
    #+""+""+""+""+""+""+""+""+
    return b
