"""
Tic-Tac-Toe (Unbeatable AI) - tic_tac_toe_ai.py

This is a simple command-line game of Tic-Tac-Toe where you (the human)
play against an AI that can never lose. The AI is powered by the
**Minimax algorithm with Alpha-Beta Pruning**, a classic approach in
game theory that ensures the computer always makes the best possible
move.

How to play:
    - Run this file with Python.
    - Pick whether you want to be X or O.
    - Choose who plays first (you or the AI).
    - Enter your move by typing a number 1–9 that corresponds to
      the positions on the board:

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9

The AI will think and make its move. The game continues until someone
wins or the board is full (a draw). Good luck beating it — spoiler: you
can’t!
"""

from typing import List, Optional, Tuple
import math
import random

# A board is represented as a list of 9 cells, each being 'X', 'O', or None
Board = List[Optional[str]]

# All possible winning lines (rows, columns, diagonals)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6)              # diagonals
]


def new_board() -> Board:
    """Start with an empty 3x3 board."""
    return [None] * 9


def pretty_board(board: Board) -> str:
    """Return a nicely formatted string representation of the board."""
    def cell(i: int) -> str:
        return board[i] if board[i] is not None else str(i + 1)

    rows = [f" {cell(r*3)} | {cell(r*3+1)} | {cell(r*3+2)} " for r in range(3)]
    sep = "\n---+---+---\n"
    return sep.join(rows)


def print_board(board: Board) -> None:
    print(pretty_board(board))


def check_winner(board: Board) -> Optional[str]:
    """Check if someone has won. Return 'X', 'O', or None."""
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_board_full(board: Board) -> bool:
    """Return True if there are no empty cells left."""
    return all(cell is not None for cell in board)


def game_over(board: Board) -> bool:
    """Return True if the game is finished (win or draw)."""
    return check_winner(board) is not None or is_board_full(board)


def available_moves(board: Board) -> List[int]:
    """Return a list of indices where moves can be played."""
    return [i for i, v in enumerate(board) if v is None]


def opponent(player: str) -> str:
    return "O" if player == "X" else "X"


def minimax(board: Board, player: str, maximizing: bool, alpha: int, beta: int) -> Tuple[int, Optional[int]]:
    """
    The Minimax algorithm with Alpha-Beta pruning.

    - If it's 'X'’s turn, we try to maximize the score.
    - If it's 'O'’s turn, we try to minimize the score.

    Scores:
        +1 -> 'X' wins
        -1 -> 'O' wins
         0 -> draw
    """
    winner = check_winner(board)
    if winner == 'X':
        return 1, None
    elif winner == 'O':
        return -1, None
    elif is_board_full(board):
        return 0, None

    best_move = None

    if maximizing:
        max_eval = -math.inf
        for mv in available_moves(board):
            board[mv] = player
            eval_score, _ = minimax(board, opponent(player), False, alpha, beta)
            board[mv] = None
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = mv
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return int(max_eval), best_move
    else:
        min_eval = math.inf
        for mv in available_moves(board):
            board[mv] = player
            eval_score, _ = minimax(board, opponent(player), True, alpha, beta)
            board[mv] = None
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = mv
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return int(min_eval), best_move


def best_move_for(board: Board, ai_player: str) -> int:


    if all(v is None for v in board):
        return random.choice([0, 2, 4, 6, 8])

    if ai_player == 'X':
        score, move = minimax(board, 'X', True, -math.inf, math.inf)
        return move
    else:
        score, move = minimax(board, 'O', False, -math.inf, math.inf)
        return move


def human_move(board: Board, human_player: str) -> int:
    
    while True:
        try:
            s = input(f"Your move ({human_player}). Enter 1-9: ")
            pos = int(s.strip()) - 1
            if pos < 0 or pos > 8:
                print("Please enter a number from 1 to 9.")
                continue
            if board[pos] is not None:
                print("That spot is already taken. Choose another.")
                continue
            return pos
        except ValueError:
            print("Please enter a valid number (1-9).")


def play_game():
    print("Welcome to Tic-Tac-Toe with an unbeatable AI!\n")

    
    while True:
        human_player = input("Do you want to be X or O? (X goes first) ").strip().upper()
        if human_player in ("X", "O"):
            break
        print("Please enter X or O.")

    ai_player = opponent(human_player)

    
    while True:
        first = input("Who moves first? (H)uman or (A)I? [default H] ").strip().upper()
        if first in ("", "H", "A"):
            break
        print("Enter H or A (or just press Enter for Human first).")

    human_turn = (first != "A")

    board = new_board()
    current = 'X'  

    while True:
        print("\nCurrent board:")
        print_board(board)

        if game_over(board):
            break

        if human_turn and current == human_player:
            pos = human_move(board, human_player)
            board[pos] = human_player
            human_turn = False
        elif not human_turn and current == ai_player:
            print("AI is thinking...")
            pos = best_move_for(board, ai_player)
            print(f"AI plays at position {pos+1} ({ai_player})")
            board[pos] = ai_player
            human_turn = True
        else:
            if current == human_player:
                pos = human_move(board, human_player)
                board[pos] = human_player
            else:
                print("AI is thinking...")
                pos = best_move_for(board, ai_player)
                print(f"AI plays at position {pos+1} ({ai_player})")
                board[pos] = ai_player
            human_turn = not human_turn

        current = opponent(current)

    print("\nFinal board:")
    print_board(board)
    winner = check_winner(board)
    if winner:
        if winner == human_player:
            print("Wow, you actually beat the AI! (This isn’t supposed to happen!)\n")
        else:
            print("AI wins. Better luck next time!\n")
    else:
        print("It's a draw!\n")


if __name__ == '__main__':
    play_game()
