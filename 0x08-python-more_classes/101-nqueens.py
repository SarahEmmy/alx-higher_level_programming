#!/usr/bin/python3
"""N-Queens Problem Solver Module
This module contains functions to search for solutions to the N-Queens problem.
"""


def all_possible(n=4):
    """ Functions:is_safe(row, col, board): 
    Check if placing a queen at the given position (row, col) on the board is safe.
    solve_n_queens(n): Solve the N-Queens problem and return a list of all possible solutions for a board of size n x n.
    """

    for x in range(n):
        matrix = []
        matrix.append([0, x])
        col = [z for z in range(n)]
        col.remove(x)
        recur_bt(matrix, 1, col, n)


def recur_bt(matrix, row, col, n):
    """
    Recursive Backtrack Function - Recursive this function is used to test 
    remaining possible positions for placing another queen on the board.
    It operates recursively and serves as the main algorithm for solving 
    the N-Queens problem. Parameters:
    matrix: A list of lists representing the positions of queens placed on the board.
    row: A list of possible row positions where the remaining queens can be placed.
    col: A list of possible column positions where the remaining queens can be placed.
    n: The size of the board and the number of queens that can be placed.
    Returns: A list of lists representing a valid solution if found, or 
    None if the current configuration leads to a dead end.
    """
    if len(matrix) is n:
        return matrix

    if row:
        x = row
        for y in col:
                if (not bot_right(matrix, x + 1, y + 1, n) or
                    not bot_left(matrix, x + 1, y - 1, n) or
                    not top_left(matrix, x - 1, y - 1, n) or
                        not top_right(matrix, x - 1, y + 1, n)):
                        continue
                matrix.append([x, y])
                new_col = list(col)
                new_col.remove(y)
                new_matrix = recur_bt(matrix, row + 1, new_col, n)
                if new_matrix is not None:
                    print(matrix)
                matrix.remove([x, y])
    return None


def bot_right(matrix, y, x, n):
    """
        Function to test if there are any queens on the bottom right diagonal.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            y (int): "row" or y co-ordinate.
                queens can be placed on.
            x (int): "column" or x co-ordinate.
            n (int): The size of the board.
        Returns:
            True if no queens exist on the bottom right diagonal of the given position, otherwise
            False.
    """
    while y < n and x < n:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x += 1
    return True


def bot_left(matrix, y, x, n):
    """
        Function to test if there are any queens on the bottom left diagonal.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            y (int): "row" or y co-ordinate.
                queens can be placed on.
            x (int): "column" or x co-ordinate.
            n (int): The size of the board.
        Returns:
            True if no queens exist on the bottom left diagonal otherwise
            False.
    """
    while y < n and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x -= 1
    return True


def top_left(matrix, y, x, n):
    """
        Function to test if there are any queens on the top left diagonal.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            y (int): "row" or y co-ordinate.
                queens can be placed on.
            x (int): "column" or x co-ordinate.
            n (int): The size of the board.
        Returns:
            True if no queens exist on the top left diagonal otherwise False.
    """
    while y >= 0 and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x -= 1
    return True


def top_right(matrix, y, x, n):
    """
        Function to test if there are any queens on the top right diagonal.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            y (int): "row" or y co-ordinate.
                queens can be placed on.
            x (int): "column" or x co-ordinate.
            n (int): The size of the board.
        Returns:
            True if no queens exist on the top right diagonal otherwise False.
    """
    while y >= 0 and x < n:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x += 1
    return True

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    all_possible(n)
