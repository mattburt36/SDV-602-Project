"""
This file contains the software which presents information to the user
It has the scope of the Model.py file, to recieve what information to be displayed to the user 
"""

import Common as c 
import Model as m 

def draw_graph():
    return 

def create_plot():
    return 

def create_window():
    """
    Function for creating a screen based on the value of the 'window_flag' variable and the layout generated from 'generate_layout'
    """
    # First generate the object of the layout from the 'model' module 
    layout = m.generate_layout()

    if c.window_flag == 0:
        # Center justify content, return the login screen 
        return c.sg.Window("Login", layout, element_justification='c')
    # INSERT REGISTRATION FORM HERE
    elif c.window_flag == 2:
        # Generate a new main screen 
        return c.sg.Window("Graph", layout, size=(900,500), finalize=True)     
    elif c.window_flag == 3:
        # Generate the map screen 
        return c.sg.Window(c.district_name, layout, no_titlebar=True)