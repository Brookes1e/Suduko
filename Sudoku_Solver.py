#!/bin/env python

"""Sudoku_Solver.py:Solves Sudokus, written to help develop the authors programming skills and become
   a custom to GitHub."""

import numpy as np
import Sudoku_Solver_File_Load
import Sudoku_GUI
from neupy.core.docs import shared_docs

__author__ = 'Harry Brookes'
__license__ = 'Apache License 2.0'
__version__ = '1.0'
__status__ = 'Development'


########################################################################################################################
# -----------------------------------------------___SUDOKU FUNCTIONS___------------------------------------------------#
########################################################################################################################


"""


"""
def in_row(row, x, y,
           input_suduko_3d):
    """
    in_row function.
        Splits suduko into in rows and removes any numbers that exist in the row from the elements third dimension.

    Parameters
    ----------
    x : int
        x axis position in the 9x9 2D suduko matrix being solved
    y : int
        y axis position in the 9x9 2D suduko matrix being solved
    input_suduko_3d : [int,int,int]
        3D matrix that  carries the current 2D matrix and all the numbers from 1-9 for each position, note that 0
            is used as a filler and dictates that the element has been removed
    """
    value_in_row = np.in1d(np.asarray(input_suduko_3d[x, y, 0:]), np.asarray(input_suduko_3d[row, :, 0]))
    for i, value in enumerate(value_in_row):
        if value_in_row[i] == True and i != 0:
            input_suduko_3d[x, y, i] = 0


@shared_docs(in_row)
def in_column(column, x, y,
              input_suduko_3d):
    """
    in_column function.
        Completes the same task as In_Row function except for columns instead

    Parameters
    ----------
    {in_row.Parameters}
    """
    value_in_column = np.in1d(np.asarray(input_suduko_3d[x, y, :]), np.asarray(input_suduko_3d[:, column, 0]))
    for i, value in enumerate(value_in_column):
        if value_in_column[i] == True and i != 0:
            input_suduko_3d[x, y, i] = 0

def blockshaped(input_suduko_2d):
    """
     blockshaped function.
        This code defines the 3x3 matrices that used for in the In_Block function

    Parameters
    ----------
    input_suduko_2d : [int,int]
        describes the current sudoku being solved, varing completed depending on the progression of the main() function
        in Sudoku_Solver.py
    """
    h = input_suduko_2d.shape[0]
    return (input_suduko_2d.reshape(h // 3, 3, -1, 3)
            .swapaxes(1, 2)
            .reshape(-1, 3, 3))

@shared_docs(in_row)
def in_block(x, y, input_suduko_3d):
    """
    in_block function.
        Removal of any values that exist in the elements 3x3 block

    Parameters
    ----------
    {in_row.Parameters}
    """
    block_id = 100

    if x < 3 and y < 3:  # First if statements defines into which block the element of given x,y values is, this are
        # from 0-8 representing the 9 boxes
        block_id = 0
    if 6 > x >= 3 > 0 <= y:
        block_id = 3
    if 6 <= x <= 8 and 0 <= y < 3:
        block_id = 6
    if x < 3 <= y < 6:
        block_id = 1
    if 3 <= x < 6 and 3 <= y < 6:
        block_id = 4
    if 8 >= x >= 6 > 3 <= y:
        block_id = 7
    if x < 3 and 6 <= y <= 8:
        block_id = 2
    if 3 <= x < 6 <= y <= 8:
        block_id = 5
    if 6 <= x <= 8 and 6 <= y <= 8:
        block_id = 8

    suduko_blocks = blockshaped(np.array(input_suduko_3d[:, :, 0]))  # suduko_blocks is a 2D array that holds all of the
        #  9 constituent block elements
    suduko_blocks_flatten = suduko_blocks[block_id].flatten()

    value_in_block = np.in1d(input_suduko_3d[x, y, :], suduko_blocks_flatten)

    for i, value in enumerate(value_in_block):
        if value_in_block[i] == True and i != 0:
            input_suduko_3d[x, y, i] = 0

########################################################################################################################
# ------------------------------------------------------___MAIN___-----------------------------------------------------#
########################################################################################################################

def main():
    user_choice = "File"
    input_file_name = "Test_input.txt"
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

            in_row(x, x, y, input_suduko_3d)
            in_column(y, x, y, input_suduko_3d)
            in_block(x, y, input_suduko_3d)

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



if __name__ == '__main__':
    main()
