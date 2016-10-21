<<<<<<< HEAD
=======

>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
import __builtin__
from kivy import require
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

import Solver_main

<<<<<<< HEAD

=======
>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
require('1.9.1')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')


<<<<<<< HEAD
class MyBox(BoxLayout):
    """MyBox defines a the basic setup of the window, implementing the grid and Solve Button widgets in a vertical
       structure

       Parameters
       ----------
       BoxLayout - imported from the kivy.uix.boxlayout module, BoxLayout is a default class that better layouts within
       the app's windows
       """
    def __init__(self):
        """Initialization of a specific instance based on the MyBox metaclass
=======


class MyBox(BoxLayout):
    """
    MyBox defines a the basic setup of the window, implementing the grid and Solve Button widgets in a vertical
    structure

    Parameters
    ----------
    BoxLayout - imported from the kivy.uix.boxlayout module, BoxLayout is a default class that better layouts within
    the app's windows
    """

    def __init__(self):
        """
        Initialization of a specific instance based on the MyBox metaclass
>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
        """
        super(MyBox, self).__init__()
        self.orientation = 'vertical'
        self.grid = MyBox.add_widget(self, Window())
        self.button = MyBox.add_widget(self, Solve())


class Window(GridLayout):
<<<<<<< HEAD
    """Windows allows for upper widget in the MyBox class to be defined as a grid system
    
    Parameters
    ––––––––––
=======
    """
    Windows allows for upper widget in the MyBox class to be defined as a grid system

    Parameters
    ----------
>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
    GridLayout from kivy.unix.gridlayout package
    """

    def __init__(self):
<<<<<<< HEAD
   """initialization of the Window class, producing a 9x9 grid to hold the individual
      elements of the array. Each element  box is defined by its own widget defined 
      by the Number_Boxes class"""
=======
        """
        initialization of the Window class, producing a 9x9 grid to hold the individual
        elements of the array. Each element  box is defined by its own widget defined
        by the Number_Boxes class
        """
>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
        super(Window, self).__init__()
        self.cols = 9
        self.rows = 9
        self.grid = [Window.add_widget(self, Number_Boxes(number=i)) for i in range(0, 81)]


class Number_Boxes(TextInput, BoxLayout):
<<<<<<< HEAD
"""The Number_Boxes class defines initializes and sets up the white boxes used to input
   The users starting sudoku
   
   Parameters
   TextInput from kivy.unix.textinput package
   BoxLayout from kivy.unix.boxlayout package
"""
    def __init__(self, number):
    """Parameters
       number calls the user input to that specific element
    """
=======
    """
    The Number_Boxes class defines initializes and sets up the white boxes used to input
    The users starting sudoku

    Parameters
    TextInput from kivy.unix.textinput package
    BoxLayout from kivy.unix.boxlayout package
    """


    def __init__(self, number):
        """
        Parameters
        number calls the user input to that specific element
        """
>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
        super(Number_Boxes, self).__init__()
        self.text = ''
        self.number = number
        self.auto_indent = True
        self.multiline = False
        self.input_filter = 'int'
        self.font_size = 28
        self.padding = [20, 5, 20, 5]

<<<<<<< HEAD
=======

>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
    def on_text_validate(self):
        if len(self.text) > 1:
            self.text = ''
            print 'You must enter a number between 0 and 9'
        else:
            print self.number, self.text
            __builtin__.saved_array[self.number] = int(self.text)


class Solve(Button):
<<<<<<< HEAD
    """The Solve class defines the button at the bottom of the GUI which allows for the
       inputted data to be passed to the back-end solver
       
       Parameters 
       Button is from kivy.unix.button
    """
    
=======
    """
    The Solve class defines the button at the bottom of the GUI which allows for the
    inputted data to be passed to the back-end solver

    Parameters
    Button is from kivy.unix.button
    """

>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
    def __init__(self):
        super(Solve, self).__init__()
        self.text = 'Solve'
        self.size_hint = (1, None)

    def on_press(self):
        Solver_main.main()
        GUI.get_running_app().stop()


class GUI(App, MyBox):
<<<<<<< HEAD
  """The GUI class brings together all of the classes defined above and implements the final call to
     produce the GUI that appears on the screen 
     
     Parameters 
     App - from kivy.app
     MyBox - from kivy.mybox
  """
   
=======
    """
    The GUI class brings together all of the classes defined above and implements the final call to
    produce the GUI that appears on the screen

    Parameters
    App - from kivy.app
    MyBox - from kivy.mybox
    """
    
>>>>>>> 664f5b066f30767c4e70447eecd31e4566faff5f
    def build(self):
        self.title = 'Sudoku'
        return self
