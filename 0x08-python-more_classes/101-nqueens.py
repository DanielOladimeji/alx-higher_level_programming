#!/usr/bin/python3

import sys


def nqueens(N):
    """ Checks if N is an integer """
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """ Checks if N is at least 4 """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """ creates an empty board """
    board = [-1] * N

    """ Checks if a queen can br placed in a given column """
    def is_valid(column, row):
        for i in range(column):
            if board[i] == row or \
                    board[i] - i == row - column or \
                    board[i] + i == row + column:
                return False
        return True

    """ Place a queen in a given column """
    def place(column):
        for row in range(N):
            if is_valid(column, row):
                board[column] = row
                if column == N - 1:
                    print_board()
                else:
                    place(column + 1)

    """ Prints the board """
    def print_board():
        for row in range(N):
            line = ""
            for column in range(N):
                if board[column] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("")

    place(0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

nqueens(sys.argv[1])
