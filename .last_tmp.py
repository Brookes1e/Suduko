import __builtin__
import logging

import Sudoku_GUI

if __name__ == "__main__":

    if Logging.DEBUG == True:
        pass
        
    __builtin__.saved_array = [0] * 81
    __builtin__.saved_array = [0, 0, 0, 0, 0, 8, 0, 9, 2,
                               1, 3, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 1, 4, 0, 6,
                               8, 4, 0, 0, 1, 6, 0, 5, 0,
                               0, 7, 0, 0, 0, 0, 0, 4, 0,
                               0, 6, 0, 9, 7, 0, 0, 2, 3,
                               7, 0, 2, 3, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 6, 5,
                               6, 9, 0, 8, 0, 0, 0, 0, 0]
    Sudoku_GUI.GUI().run()