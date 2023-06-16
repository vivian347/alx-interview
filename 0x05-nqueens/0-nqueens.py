#!/usr/bin/python3

import sys


def solve_nqueens(N):
    # Check if N is a number
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard as a list of length N, with all elements set to -1
    board = [-1] * N
    solutions = []

    def is_safe(row, col):
        # Check if the current position is safe for a queen
        for i in range(row):
            # Check if there is a queen in the same column or diagonals
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def place_queen(row):
        # Recursive function to place queens on the board row by row
        if row == N:
            # If all queens are placed, add the solution to the list of solutions
            solutions.append([(i, board[i]) for i in range(N)])
            return
        for col in range(N):
            if is_safe(row, col):
                # If the current position is safe, place the queen and move to the next row
                board[row] = col
                place_queen(row + 1)

    # Start solving from the first row
    place_queen(0)

    # Print each solution
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
