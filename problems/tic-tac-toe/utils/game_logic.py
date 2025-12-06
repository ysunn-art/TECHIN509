from models.board import Board
from models.player import Player
from utils.record_data import store_game_data


def play_tic_tac_toe():
    """
    Implement the logic of a Tic Tac Toe game.
    Two players take turn to mark the board. 
    The logic checks winner at each turn.
    """
    board = Board()
    # Instatiate a human player making random moves
    player1 = Player("X")
    # Instatiate a robot player making random moves
    player2 = Player("O", random=True) 
    current_player = player1
    first_player = current_player.symbol

    while True:
        board.draw_board()
        print(f"{current_player.symbol} player's turn.")

        if current_player.random:
            max_attempts = 5  # Limit for random player attempts
            for _ in range(max_attempts):
                row, col = current_player.get_move()
                if board.update_board(row, col, current_player.symbol):
                    break  # Move successful, exit retry loop
            else:
                # Skip turn if all attempts fail
                print(f"{current_player.symbol} player could not make a valid move after {max_attempts} attempts.")
                current_player = player2 if current_player == player1 else player1
                continue
        else:
            # Handle human player's move
            while True:
                row, col = current_player.get_move()
                if board.update_board(row, col, current_player.symbol):
                    break
                print("That cell is occupied. Try again.")

        # Check if the current player has won
        winner = board.check_winner()
        if winner:
            board.draw_board()
            print(f"{winner} player win!")
            store_game_data(
                filename="data/game_data.csv",
                first_player=first_player,
                winner=current_player.symbol
            )
            break

        # Check if the board is full
        if board.is_full():
            board.draw_board()
            print("It's a draw!")
            store_game_data(
                filename="data/game_data.csv",
                first_player=first_player,
                winner="Draw"
            )
            break

        # Switch to the next player
        current_player = player2 if current_player == player1 else player1
