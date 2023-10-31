#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row:
            return False
        if board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(n, row, board, solutions):
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(n, row + 1, board, solutions)


def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    solve_n_queens_util(n, 0, board, solutions)
    return solutions


def print_solution(solution):
    print("[" + ', '.join([str(pos) for pos in solution]) + "]")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = solve_n_queens(N)
        for solution in solutions:
            print_solution(solution)
            print()

    except ValueError:
        print("N must be a number")
        sys.exit(1)
