import __builtin__
import traceback

import Sudoku_Solver
import numpy as np


########################################################################################################################
# ------------------------------------------------------___MAIN___-----------------------------------------------------#
########################################################################################################################

def main():

    try:
        SOLVED_FLAG = False  # Solved flag initialisation
        LOOP_FLAG = 0

        input_suduko = __builtin__.saved_array

        if np.count_nonzero(input_suduko) < 17:
            raise Exception("This Sudoku is unsolvable and must have at least 17 non zero elements")

        input_suduko_2d = [np.array(input_suduko)[i:i + 9] for i in range(0, len(input_suduko), 9)]
        input_suduko_3d = np.zeros((9, 9, 10))
        input_suduko_3d[:, :, 0] = input_suduko_2d

        for i in range(1, 10):
            input_suduko_3d[:, :, i] = i

        while not SOLVED_FLAG:

            if LOOP_FLAG > 150:
                raise Exception("This Soduku is Unsolvable")

            for (x, y), value in np.ndenumerate(input_suduko_3d[:, :, 0]):

                if input_suduko_3d[x, y, 0] != 0:
                    # Clear values that are in the third dimension behind a predefined value in the suduko
                    # puzzle, no advantage except for visual debugging of potential element values
                    for i in range(1, 10):
                        input_suduko_3d[x, y, i] = '100'

                Sudoku_Solver.in_row(x, x, y, input_suduko_3d)
                Sudoku_Solver.in_column(y, x, y, input_suduko_3d)
                Sudoku_Solver.in_block(x, y, input_suduko_3d)

            for (x, y), value_input_sudoku in np.ndenumerate(input_suduko_3d[:, :, 0]):
                maybe = []
                for i, value in enumerate(input_suduko_3d[x, y, 1:]):
                    if value != 0:
                        maybe.append(value)

                if len(maybe) == 1:
                    input_suduko_3d[x, y, 0] = maybe[0]

            if 0 not in input_suduko_3d[:, :, 0]:
                SOLVED_FLAG = True
                __builtin__.saved_array = input_suduko_3d[:, :, 0]
                print __builtin__.saved_array

            LOOP_FLAG += 1

    except Exception, ERROR:
        ERROR
