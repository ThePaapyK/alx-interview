#!/usr/bin/python3
"""The N queens puzzle """


import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check if there is a queen in the diagonal
        if board[i] - i == col - row or board[i] + i == col + row:
            return False

    return True

def solve_nqueens(N):
    board = [-1] * N
    solutions = []

    def backtrack(row):
        nonlocal solutions
        if row == N:
            # Found a solution, add it to the list
            solutions.append(board.copy())
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)

    return solutions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        for row in solution:
            print([i, row] for i in range(N))
        print()

