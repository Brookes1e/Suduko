import Sudoku_Solver_File_Load
import Sudoku_GUI
import Sudoku_Solver
import numpy as np


########################################################################################################################
# ------------------------------------------------------___MAIN___-----------------------------------------------------#
########################################################################################################################



user_choice = 'File'
input_file_name = 'Suduko/Test_input.txt'
input_suduko = Sudoku_Solver_File_Load.load(user_choice, input_file_name)

solved = False  # Solved flag initialisation

input_suduko_2d = [input_suduko[i:i + 9] for i in range(0, len(input_suduko), 9)]
input_suduko_3d = np.zeros((9, 9, 10))
input_suduko_3d[:, :, 0] = input_suduko_2d

Sudoku_GUI.draw(input_suduko_3d[:, :, 0])

for i in range(1, 10):
    input_suduko_3d[:, :, i] = i

while not solved:

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
            Sudoku_GUI.draw(input_suduko_3d[:, :, 0])

    if 0 not in input_suduko_3d[:, :, 0]:
        solved = True
        print input_suduko_3d[:, :, 0]
