#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve(board, col, N, result):
    if col == N:
        result.append([''.join(['Q' if x else '.' for x in row]) for row in board])
        return True
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve(board, col + 1, N, result) or res
            board[i][col] = 0
    return res

def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    if not solve(board, 0, N, result):
        print("No solution exists")
        sys.exit(1)

    for solution in result:
        print("\n".join(solution))
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
