import os

def Input_Test(input_file):

    if input_file == None:
        raise "Please input a valid sudoku array\n"

    if len(input_file) != 81:
        raise "The current input file is not a valid 81 length array\n"

    print "The current input file has been loaded successfully\n"

def Check_File_Exists(input_file_name):
    if os.path.isfile(input_file_name):
        return True
    else:
        raise "Not a valid file name"

