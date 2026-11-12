
import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [""] * 9
buttons = []


def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    return None


def make_move(index):
    global current_player

    if board[index] != "":
        return

    board[index] = current_player
    buttons[index].config(
        text=current_player,
        state="disabled",
        disabledforeground="blue" if current_player == "X" else "red"
    )

    winner = check_winner()

    if winner:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        reset_game()
        return

    if "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
        return

    current_player = "O" if current_player == "X" else "X"
    status.config(text=f"Player {current_player}'s Turn")


def reset_game():
    global current_player, board

    current_player = "X"
    board = [""] * 9

    for button in buttons:
        button.config(text="", state="normal")

    status.config(text="Player X's Turn")


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x480")
root.resizable(False, False)
root.configure(bg="#20232a")

title = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 25, "bold"),
    bg="#20232a",
    fg="white"
)
title.pack(pady=20)

status = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 16),
    bg="#20232a",
    fg="#61dafb"
)
status.pack(pady=10)

game_frame = tk.Frame(root, bg="#20232a")
game_frame.pack(pady=15)

for i in range(9):
    button = tk.Button(
        game_frame,
        text="",
        font=("Arial", 28, "bold"),
        width=5,
        height=2,
        bg="#eeeeee",
        command=lambda index=i: make_move(index)
    )
    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )
    buttons.append(button)

restart_button = tk.Button(
    root,
    text="RESTART GAME",
    font=("Arial", 13, "bold"),
    bg="#61dafb",
    fg="black",
    command=reset_game
)
restart_button.pack(pady=20)

root.mainloop()
