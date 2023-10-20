import tkinter as tk
import sys
from tkinter import messagebox

# create the 3x3 board
board = [[' ' for _ in range(3)] for _ in range(3)]

# set player and ai
PLAYER = 'X'
OPPONENT_AI = 'O'

# display 'X' or 'O' in the board
labels = [[None for _ in range(3)] for _ in range(3)]

# score of player and ai, initially set it to 0
player_score = 0
ai_score = 0

# check if the cell is empty or not
def is_empty_cell():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    return False

# evaluate for victory
def evaluate():
    # check rows for victory
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == PLAYER:
                return 10
            elif board[row][0] == OPPONENT_AI:
                return -10

    # check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == PLAYER:
                return 10
            elif board[0][col] == OPPONENT_AI:
                return -10

    # check 1st diagonal for victory
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == PLAYER:
            return 10
        elif board[0][0] == OPPONENT_AI:
            return -10

    # check 2nd diagonal for victory
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == PLAYER:
            return 10
        elif board[0][2] == OPPONENT_AI:
            return -10
    # check for no victory or no winner
    return 0
# ---------------------------------------------------------------------------------------------------

# mimimax implementation
def minimax(depth, is_maximizing):
    score = evaluate()

    # If the maximizer or minimizer wins the game, return the score, -10 for AI and 10 for player
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth

    # check if there remains empty cell
    if not is_empty_cell():
        return 0

    # maximizer turn
    if is_maximizing:
        best_score = -sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    best_score = max(best_score, minimax(
                        depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best_score

    # minimizer turn
    else:
        best_score = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = OPPONENT_AI
                    best_score = min(best_score, minimax(
                        depth + 1, not is_maximizing))
                    board[i][j] = ' '
        return best_score

# check for best move
def find_best_move():
    best_score = -sys.maxsize
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER
                score = minimax(0, False)
                board[i][j] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move





def player_move(row, col):
    if board[row][col] == ' ' and evaluate() == 0:
        board[row][col] = PLAYER
        labels[row][col]['text'] = PLAYER
        labels[row][col]['state'] = 'disabled'
        ai_move()


def ai_move():
    if evaluate() == 0 and is_empty_cell():
        move = find_best_move()
        row, col = move
        board[row][col] = OPPONENT_AI
        labels[row][col]['text'] = OPPONENT_AI
        labels[row][col]['state'] = 'disabled'

# --------------------GUI_part------------------------------------------


# create GUI using tkinter
game_window = tk.Tk()
game_window.title("AI tic-tac-toe")

# create 3x3 labels button
for i in range(3):
    for j in range(3):
        labels[i][j] = tk.Button(game_window, text=" ", width=30,
                                 height=9, command=lambda row=i, col=j: player_move(row, col))
        labels[i][j].grid(row=i, column=j)

# player score and AI score
player_score_label = tk.Label(game_window, text=f"Player: {player_score}")
player_score_label.grid(row=3, column=0)
ai_score_label = tk.Label(game_window, text=f"AI: {ai_score}")
ai_score_label.grid(row=3, column=1)


# initially set game state to false
game_started = False

# reset the game board
def reset_board():
    global board
    global game_started
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
            labels[i][j]['text'] = ' '
            labels[i][j]['state'] = 'active'
    game_started = False


# start the game
def start_game():
    global game_started
    if not game_started:
        reset_board()
        game_started = True
        play_game()

# play game and result function
def play_game():
    global player_score
    global ai_score
    while is_empty_cell() and evaluate() == 0:
        game_window.update()
    # this will show the result after the game
    if evaluate() > 0:
        player_score += 1
        player_score_label.config(text=f"Player: {player_score}")
        messagebox.showinfo("Game Over", "Player wins!")
    elif evaluate() < 0:
        ai_score += 1
        ai_score_label.config(text=f"AI: {ai_score}")
        messagebox.showinfo("Game Over", "AI wins!")
    else:
        messagebox.showinfo("Game Over", "It's a tie!")

# exit the game
def exit_game():
    print('Game ended. Thank You for Playing Tic-Tac-Toe')
    game_window.destroy()


# create start, reset, and exit buttons
start_button = tk.Button(game_window, text="Start", command=start_game)
start_button.grid(row=4, column=0)

reset_button = tk.Button(game_window, text="Reset", command=reset_board)
reset_button.grid(row=4, column=1)

exit_button = tk.Button(game_window, text="Exit", command=exit_game)
exit_button.grid(row=4, column=2)


# main game loop
def main():
    print("Game started")


if __name__ == "__main__":
    main()
    game_window.mainloop()
