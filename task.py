# Matrix.


# Write a class that can represent any 4𝑥4 real matrix.
# Include two functions to calculate the sum and dot product of two matrices.
# Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
# Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction
# - inversion
# - string representation
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
# Delete these comments before commit!
#
# Good luck.

class Matrix:
    def __init__(self, row1, row2, row3, row4):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4
        self.columns = 4
        self.rows = 4

    def add(self, matrix_1, matrix_2):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                matrix_res[i][j] = matrix_1[i][j] + matrix_2[i][j]
                return matrix_res


matrix1 = ([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4])
print()
