import tkinter as tk
from tkinter import messagebox

# Board Setup
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("460x415")

current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Functin
def check_win(player):
    # Rows and columns
    for i in range(3):
        if all(buttons[i][j]["text"] == player for j in range(3)) or \
           all(buttons[j][i]["text"] == player for j in range(3)):
            return True
    # Diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player or \
       buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player:
        return True
    return False
#draw
def check_draw():
    return all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))
#reset
def reset_board():
    global current_player
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
    current_player = "X"

def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        # Set color: X → red, O → black
        if current_player == "X":
            buttons[row][col]["fg"] = "red"
        else:
            buttons[row][col]["fg"] = "black"

        if check_win(current_player):
            messagebox.showinfo("Tic Tac Toe", f"Si Player {current_player} ang malakas!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"


# ----- Create Buttons -----
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Courier New", 36), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# ----- Run the GUI -----
root.mainloop()
