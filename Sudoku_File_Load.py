import Sudoku_Errors

def Main(user_choice, input_file_name):
    if user_choice == "File" and Sudoku_Errors.Check_File_Exists(input_file_name):
        file_open = open(input_file_name, "r")
        input_file = list(file_open.read())
        Sudoku_Errors.Input_Test(input_file)
        return input_file

if __name__ == '__main__': Main()
