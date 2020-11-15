import logging
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

logging.basicConfig(level=logging.ERROR, format='%(levelname)-10s %(message)s')


class Matrix:
    def __init__(
        self, matrix_dimension, rows=0
    ):
        self.matrix_dimension = matrix_dimension

        if rows == 0:
            self.rows = [[0]*matrix_dimension for i in range(matrix_dimension)]
        else:
            self.rows = []
            for i in rows:
                if len(i) == matrix_dimension:
                    self.rows.append(i)
                else:
                    self.rows = []
                    logging.error("Wrong row dimension! It must has {itm} items instead of {itm_has}.".format(
                        itm=matrix_dimension, itm_has=len(i)))
                    break

    def __setitem__(
        self, index, item
    ):
        if len(item) == self.matrix_dimension:
            self.rows[index] = item
        else:
            logging.error("Wrong row dimension! It must has {itm} items. Matrix has not been changed.".format(
                itm=self.matrix_dimension))

    def __getitem__(
        self, index
    ):
        return self.rows[index]

    def __str__(self):
        str1 = ''
        for i in self.rows:
            for x in i:
                str1 = str1 + str(x) + ' '
            str1 += '\n'
        return str1

    def __add__(
        self, matrix
    ):
        matrix_res = Matrix(self.matrix_dimension)
        for i in range(self.matrix_dimension):
            for j in range(self.matrix_dimension):
                matrix_res[i][j] = self.rows[i][j] + matrix[i][j]
        return matrix_res

    def __sub__(
        self, matrix
    ):
        matrix_res = Matrix(self.matrix_dimension)
        for i in range(self.matrix_dimension):
            for j in range(self.matrix_dimension):
                matrix_res[i][j] = self.rows[i][j] - matrix[i][j]
        return matrix_res

    def __mul__(
        self, matrix
    ):
        matrix_res = Matrix(self.matrix_dimension)
        for i in range(self.matrix_dimension):
            for j in range(self.matrix_dimension):
        return matrix_res


m1 = Matrix(3)
m1[0] = [1, 2, 3]
m1[1] = [1, 2, 3]
m1[2] = [1, 2, 3]
print(
    "Creation of matrix filled with zeros. Then setting particular rows ( m[row] ):\n{}".format(m1))

m2 = Matrix(3, [[5, 4, 5], [4, 2, 4], [3, 1, 6]])
print(
    "Creation of matrix by passing rows as arguments in constructor function:\n{}".format(m2))

m3 = m1 + m2
print(
    "Result of addition of 2 matrices:\n{}".format(m3))

m3 = m1 - m2
print(
    "Result of subtraction of 2 matrices:\n{}".format(m3))
