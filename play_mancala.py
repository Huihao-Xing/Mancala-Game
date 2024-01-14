from mancala_helpers import *

def get_valid_move(player, board):
    moves = list(map(str, valid_moves(player, board)))
    prompt = "Player %d, enter a move (%s): " % (player, ",".join(moves))
    while True:
        move = input(prompt)
        if move in moves: return int(move)
        print("Invalid move, try again.")

if __name__ == "__main__":

    board = initial_board()
    
    player = 0
    while is_not_over(board):

        print(string_of(board))
        move = get_valid_move(player, board)
        player, board = play_turn(move, board)
    
    print(string_of(board))
    print("Clearing pits...")
    board = clear_pits(board)

    print(string_of(board))
    if is_tied(board):
        print("Game over, it is tied.")
    else:
        winner = winner_of(board)
        print("Game over, player %d wins." % winner)

