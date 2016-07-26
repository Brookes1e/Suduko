"""Sudoku_Solver_File_Load.py: Functions used to load a user defined sudoku in the Sudoku_Solver.py script,
0 represent unknown vales of the sudoku"""

import Sudoku_Solver_Errors

__version__ = '1.0'
__status__ = 'Development'


def load(user_choice, input_file_name):
    if user_choice == "File" and Sudoku_Solver_Errors.check_file_exists(input_file_name):
        file_open = open(input_file_name, "r")
        input_file = list(file_open.read())
        Sudoku_Solver_Errors.input_test(input_file)
        print "The current input file has been loaded successfully\n"
        return input_file


