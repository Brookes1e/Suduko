__author__ = 'Harry Brookes'

import numpy as np
import Sudoku_Errors
import Sudoku_File_Load


def In_Row(row, x, y,
           input_suduko_3D):  ##### Splits suduko into in rows and removes any numbers that exist in the row from the elements third dimension
    value_in_row = np.in1d(np.asarray(input_suduko_3D[x, y, 0:]), np.asarray(input_suduko_3D[row, :, 0]))
    for i, value in enumerate(value_in_row):
        if value_in_row[i] == True and i != 0:
            input_suduko_3D[x, y, i] = 0  ##### Removal of element is defined as conversion to 0 value


def In_Column(column, x, y,
              input_suduko_3D):  ##### Completes the same task as In_Row fucntion except fro columns instead
    value_in_column = np.in1d(np.asarray(input_suduko_3D[x, y, :]), np.asarray(input_suduko_3D[:, column, 0]))
    for i, value in enumerate(value_in_column):
        if value_in_column[i] == True and i != 0:
            input_suduko_3D[x, y, i] = 0


def Blockshaped(arr, nrows, ncols):  ##### This code defines the 3x3 matrixes that used for in the In_Block function
    h, w = arr.shape
    return (arr.reshape(h // nrows, nrows, -1, ncols)
            .swapaxes(1, 2)
            .reshape(-1, nrows, ncols))


def In_Block(x, y, input_suduko_3D):  ##### Removal of any values that exist in the elements 3x3 block
    if x < 3 and y < 3:  ##### First if statements defines into which block the element of given x,y values is, this are from 0-8 representing the 9 boxes
        block_id = 0
    if 3 <= x < 6 and 0 <= y < 3:
        block_id = 3
    if 6 <= x <= 8 and 0 <= y < 3:
        block_id = 6
    if x < 3 and 3 <= y < 6:
        block_id = 1
    if 3 <= x < 6 and 3 <= y < 6:
        block_id = 4
    if 6 <= x <= 8 and 3 <= y < 6:
        block_id = 7
    if x < 3 and 6 <= y <= 8:
        block_id = 2
    if 3 <= x < 6 and 6 <= y <= 8:
        block_id = 5
    if 6 <= x <= 8 and 6 <= y <= 8:
        block_id = 8

    suduko_blocks = Blockshaped(np.array(input_suduko_3D[:, :, 0]), 3,
                                3)  ##### suduko_blocks is a 2D array that holds all of the 9 constient block elements
    suduko_blocks_flatten = suduko_blocks[block_id].flatten()

    value_in_block = np.in1d(input_suduko_3D[x, y, :], suduko_blocks_flatten)

    for i, value in enumerate(value_in_block):
        if value_in_block[i] == True and i != 0:
            input_suduko_3D[x, y, i] = 0


########################################################################################################################
# ------------------------------------------------------___MAIN___-----------------------------------------------------#
########################################################################################################################

def Main():
    user_choice = "File"
    input_file_name = "Test_input.txt"
    input_suduko = Sudoku_File_Load.Main(user_choice, input_file_name)

    solved = False  ##### Solved flag initilisation

    input_suduko_2d = [input_suduko[i:i + 9] for i in range(0, len(input_suduko), 9)]
    input_suduko_3d = np.zeros((9, 9, 10))
    input_suduko_3d[:, :, 0] = input_suduko_2d

    for i in range(1, 10):
        input_suduko_3d[:, :, i] = i

    while (not solved):
        input_suduko_2d = [input_suduko_3d.flatten()[i:i + 9] for i in range(0, len(input_suduko_3d.flatten()), 9)]

        for (x, y), value in np.ndenumerate(input_suduko_3d[:, :, 0]):

            if input_suduko_3d[
                x, y, 0] != 0:  #####clear values that are in the thrid dimension behind a predefined value in the suduko puzzle, no advantage except for visual debugging of potential element values
                for i in range(1, 10):
                    input_suduko_3d[x, y, i] = '100'

            In_Row(x, x, y, input_suduko_3d)
            In_Column(y, x, y, input_suduko_3d)
            In_Block(x, y, input_suduko_3d)

        for (x, y), value in np.ndenumerate(input_suduko_3d[:, :, 0]):
            maybe = []
            for i, value in enumerate(input_suduko_3d[x, y, 1:]):
                if value != 0:
                    maybe.append(value)

            if len(maybe) == 1:
                input_suduko_3d[x, y, 0] = maybe[0]

        if 0 not in input_suduko_3d[:, :, 0]:
            solved = True
            print input_suduko_3d[:, :, 0]


if __name__ == '__main__': Main()
