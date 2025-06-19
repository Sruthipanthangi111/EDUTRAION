import math

# Initialize board
board = [" " for _ in range(9)]

# Display board
def print_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print("|".join(row))
        if i < 2:
            print("-"*5)
 
# Check for winner
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    return any(all(board[pos] == player for pos in line) for line in win_conditions)

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game
def play():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()
    
    while True:
        # Human turn
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if board[move] != " " or move not in range(9):
                print("Invalid move. Try again.")
                continue
            board[move] = "X"
        except:
            print("Enter a number between 1 and 9.")
            continue
        
        print_board()

        if check_winner("X"):
            print("You win!")
            break
        elif is_draw():
            print("It's a draw!")
            break

        # AI turn
        ai_move()
        print("\nAI's move:")
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        elif is_draw():
            print("It's a draw!")
            break

# Run the game
if __name__== "__main__":
    play()
 