"""
This file contains the software which presents information to the user
It has the scope of the Model.py file, to recieve what information to be displayed to the user 
"""
import Common as c 
import Model as m 

def draw_figure(canvas, figure):    
    figure_canvas_agg = c.FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def create_plot(x, y, flag):
    """
    Function to plot graph values, switch between types of graph to be plotted 
    """
    # Dispose any past graphs that were plotted 
    c.plt.cla()
    c.plt.clf()
    
    # State machine to switch between bar graph plotting and line graph plotting 
    if flag == 0:
        c.plt.plot(x, y, color="blue", marker="o")
    elif flag == 1: 
        c.plt.bar(x,y,color="green")
        c.plt.plot()

    c.plt.title(f'Food prices: {c.district_list}')
    c.plt.xlabel("Years")
    c.plt.ylabel("Price")
    c.plt.grid(True)
    return c.plt.gcf()

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
        return c.sg.Window("Graph", layout, size=(900,525), finalize=True)     
    elif c.window_flag == 3:
        # Generate the map screen 
        return c.sg.Window(c.district_name, layout, no_titlebar=True)