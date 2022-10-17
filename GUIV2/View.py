from xml.etree.ElementTree import tostring
import Common as com
import Model as mod

def draw_graph(canvas, figure):
    """
    Function to draw a graph 
    """
    figure_canvas_agg = com.FigureCanvasTkAgg(figure, canvas)    
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def create_plot(x, flag):
    """
    Function to plot graph values, switch between types of graph to be plotted 
    """
    # Dispose any past graphs that were plotted 
    com.plt.cla()
    com.plt.clf()
    y = mod.find_average(com.graph_years_list, com.selected_commodity, com.district_name)

    # print(y,com.selected_commodity)
    # State machine to switch between bar graph plotting and line graph plotting 
    if flag == 0:
        com.plt.plot(x, y, color="blue", marker="o")
    elif flag == 1: 
        com.plt.bar(x,y,color="green")
        com.plt.plot()

    com.plt.title(f'Average price of {com.selected_commodity} in {com.district_name}')
    com.plt.xlabel("Year")
    com.plt.ylabel("Price ($)")
    com.plt.grid(True)
    return com.plt.gcf()

def create_window():
    """
    Function for creating a screen based on the value of the 'window_flag' variable and the layout generated from 'generate_layout'
    """
    # First generate the object of the layout from the 'model' module 
    layout = mod.generate_layout()

    if com.window_flag == 0:
        # Center justify content, return the login screen 
        return com.sg.Window("Login", layout, element_justification='c')
    elif com.window_flag == 1:
        # Generate a new main screen 
        return com.sg.Window("Main", layout, size=(900,525), finalize=True)     
    elif com.window_flag == 2:
        # Generate the map screen 
        return com.sg.Window(com.district_name, layout, no_titlebar=True)
