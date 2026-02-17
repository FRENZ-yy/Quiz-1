board = [" "," "," ",
         " "," "," ",
         " "," "," "]

def display_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw():
    return all(space != " " for space in board)

def play_game():
    current_player = "X"
    
    while True:
        display_board(board)
        
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            
            if move < 0 or move > 8:
                print("Invalid position. Choose 1-9.")
                continue

            if board[move] == " ":
                board[move] = current_player

                if check_win(current_player):
                    display_board(board)
                    print(f"Player {current_player} wins!")
                    break

                elif check_draw():
                    display_board(board)
                    print("It's a draw!")
                    break

                current_player = "O" if current_player == "X" else "X"

            else:
                print("That space is already taken. Try again.")

        except ValueError:
            print("Please enter a valid number.")

play_game()
