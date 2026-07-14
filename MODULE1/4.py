import random


# Function to display the Tic-Tac-Toe board
def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


# Function to let the player choose X or O
def player_choice():
    while True:
        symbol = input("Do you want to be X or O? ").upper()

        if symbol == "X":
            return "X", "O"

        elif symbol == "O":
            return "O", "X"

        else:
            print("Please enter either X or O.")


# Function for the player's move
def player_move(board, symbol):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))

            if move not in range(1, 10):
                print("Please choose a number between 1 and 9.")

            elif not board[move - 1].isdigit():
                print("That position is already taken.")

            else:
                board[move - 1] = symbol
                break

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function for the AI's move
def ai_move(board, ai_symbol, player_symbol):

    # Try to win
    for i in range(9):
        if board[i].isdigit():
            temp_board = board.copy()
            temp_board[i] = ai_symbol

            if check_win(temp_board, ai_symbol):
                board[i] = ai_symbol
                return

    # Block the player's winning move
    for i in range(9):
        if board[i].isdigit():
            temp_board = board.copy()
            temp_board[i] = player_symbol

            if check_win(temp_board, player_symbol):
                board[i] = ai_symbol
                return

    # Otherwise choose a random empty position
    empty_positions = [i for i in range(9) if board[i].isdigit()]
    random_move = random.choice(empty_positions)
    board[random_move] = ai_symbol


# Function to check if a player has won
def check_win(board, symbol):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for position in winning_positions:
        if (
            board[position[0]] == symbol and
            board[position[1]] == symbol and
            board[position[2]] == symbol
        ):
            return True

    return False


# Function to check if the board is full
def check_full(board):
    return all(not cell.isdigit() for cell in board)


# Main game function
def tic_tac_toe():
    print("🎮 Welcome to Tic-Tac-Toe!")

    player_name = input("Enter your name: ").strip()

    if player_name == "":
        player_name = "Player"

    while True:

        # Create a new board
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        player_symbol, ai_symbol = player_choice()

        turn = "Player"
        game_running = True

        while game_running:

            display_board(board)

            if turn == "Player":

                player_move(board, player_symbol)

                if check_win(board, player_symbol):
                    display_board(board)
                    print(f"🎉 Congratulations, {player_name}! You won!")
                    game_running = False

                elif check_full(board):
                    display_board(board)
                    print("It's a tie!")
                    game_running = False

                else:
                    turn = "AI"

            else:

                print("AI is making a move...\n")
                ai_move(board, ai_symbol, player_symbol)

                if check_win(board, ai_symbol):
                    display_board(board)
                    print("AI wins the game!")
                    game_running = False

                elif check_full(board):
                    display_board(board)
                    print("It's a tie!")
                    game_running = False

                else:
                    turn = "Player"

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("Thanks for playing! 👋")
            break


# Run the game
if __name__ == "__main__":
    tic_tac_toe()