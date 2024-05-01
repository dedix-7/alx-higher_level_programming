#!/usr/bin/python3
""" A module to solve the n queens problem
"""
import sys


if (len(sys.argv) != 2):
    print("Usage: nqueens N")
    sys.exit(1)
arg = sys.argv[1]
try:
    r = int(arg)
except Exception:
    print('N must be a number')
    sys.exit(1)
if (type(r) is not int):
    print('N must be a number')
    sys.exit(1)
if (r < 4):
    print("N must be at least 4")
    sys.exit(1)


def issafe(row, col, board, n):
    """ function to check whether the position is safe
    """

    duprow = row
    dupcol = col

    while((row >= 0) and (col >= 0)):
        if (board[row][col] == 'Q'):
            return False
        row -= 1
        col -= 1
    col = dupcol
    row = duprow
    while (col >= 0):
        if (board[row][col] == 'Q'):
            return False
        col -= 1
    row = duprow
    col = dupcol

    while (row < n and col >= 0):
        if (board[row][col] == 'Q'):
            return False
        row += 1
        col -= 1

    return True


def solve(col, board, ans, n):
    """ The function to actually solve the problem
    """

    if (col == n):
        ans.append(board)
        return
    for row in range(n):
        if (issafe(row, col, board, n)):
            board[row][col] = 'Q'
            solve(col + 1, board, ans, n)
            board[row][col] = '.'

def solvenqueens(r):
    n = r
    ans = [[]]
    board = [[]]
    row = []
    for t in range(n):
        for r in range(n):
            row.append('.')
        board.append(row)
    solve(0, board, ans, n)
    return (ans)

answer = solvenqueens(r)
print(answer)
