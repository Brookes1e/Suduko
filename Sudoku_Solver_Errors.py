"""Sudoku_Solver_Errors.py: Functions used to complete error analysis in the Sudoku_Solver.py script."""

import os

__version__ = '1.0'
__status__ = 'Development'


def input_test(input_file):
    if len(input_file) != 81:
        raise Exception("The current input file is not a valid 81 length array\n")


def check_file_exists(input_file_name):
    if os.path.isfile(input_file_name):
        return True
    else:
        raise Exception("Not a valid file name")
