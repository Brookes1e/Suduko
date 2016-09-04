

import os

__version__ = '1.0'
__status__ = 'Development'

def input_test(input_array):
    """
    input_test function.
        checks that the array returned is 81 elements long, raises an exeption if not true.

    Parameters
    ----------
    input_array : [int]
        holds the array loaded from the file.

    """
    if len(input_array) != 81:
        raise Exception("The current input file is not a valid 81 length array\n")


def check_file_exists(input_file_name):
    """
    check_file_exists function.
        checks that the given file name actually represents a file, raises an exeption is not true.

    Parameters
    ----------
    input_file_name : str
        name given by the user for checking.
    """
    if os.path.isfile(input_file_name):
        return True
    else:
        raise Exception("Not a valid file name")
