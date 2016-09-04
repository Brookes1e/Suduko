"""Sudoku_Solver_File_Load.py: Functions used to load a user defined sudoku in the Sudoku_Solver.py script,
0 represent unknown vales of the sudoku"""

from Sudoku_Solver_Errors import check_file_exists,input_test
from neupy.core.docs import shared_docs

__version__ = '1.0'
__status__ = 'Development'

@shared_docs(check_file_exists)
def load(user_choice, input_file_name):
    """
    load function.
        Loads a specific file defining the sudokus intial starting conditions

    Parameter
    ---------
    {check_file_exists.input_file_name}
    user_choice : str
        holds the user selection for the method of input of the data, DEVELOPMENT
    """
    if user_choice == "File" and check_file_exists(input_file_name):
        file_open = open(input_file_name, "r")
        input_file = list(file_open.read())
        input_test(input_file)
        print "The current input file has been loaded successfully\n"
        return input_file


