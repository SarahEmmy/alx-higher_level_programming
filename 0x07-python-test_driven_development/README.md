0x07. Python - Test-driven development
Python
UnitTests
TDD

Important notice on intranet checks for Python projects
Starting from today:

Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
Don’t trust the user, always think about all possible edge cases
Resources
Read or watch:

doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)
doctest – Testing through documentation
Unit Tests in Python
Unittest module
Interactive and Non-interactive tests
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# Integers addition
def add_integer(a, b):
    """
    Add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of 'a' and 'b'.
    """
    return a + b


# Divide a matrix
def divide_matrix(matrix, divisor):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        divisor (int): The number to divide each element by.

    Returns:
        list of lists: The resulting matrix after division.
    """
    result = [[element / divisor for element in row] for row in matrix]
    return result


# Say my name
def say_my_name(name):
    """
    Print "My name is" followed by the given name.

    Args:
        name (str): The name to be printed.
    """
    print("My name is", name)


# Print square
def print_square(size):
    """
    Print a square with the character '#'.

    Args:
        size (int): The size of the square (number of rows and columns).
    """
    for _ in range(size):
        print("#" * size)


# Text indentation
def print_indented_text(text):
    """
    Print a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The text to be printed.
    """
    for char in text:
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n" * 2, end="")
    print()


# Max integer - Unittest
def max_integer(numbers):
    """
    Find the maximum integer from a list of numbers.

    Args:
        numbers (list): List of integers.

    Returns:
        int: The maximum integer from the list.
    """
    return max(numbers)


# Matrix multiplication
def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices and return the resulting matrix.

    Args:
        matrix1 (list of lists): The first matrix.
        matrix2 (list of lists): The second matrix.

    Returns:
        list of lists: The resulting matrix after multiplication.
    """
    result = [[sum(a * b for a, b in zip(row1, col2)) for col2 in zip(*matrix2)] for row1 in matrix1]
    return result


# Lazy matrix multiplication
def lazy_multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices using NumPy module and return the resulting matrix.

    Args:
        matrix1 (ndarray): The first matrix.
        matrix2 (ndarray): The second matrix.

    Returns:
        ndarray: The resulting matrix after multiplication.
    """
    import numpy as np
    result = np.matmul(matrix1, matrix2)
    return result

