"""
This file houses variables and libraries for the main GUI, it is to be accessible and visible by each other module  
"""
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from decimal import *
import Model as m

# Set some initial conditions
sg.theme('DarkTeal10')  
graph_flag = 0
window_flag = 0
district_name = 'Kyiv'
selected_commodity = 'Milk'
begin_year = 2014
end_year = 2022
graph_years_list = list(range(begin_year, (end_year + 1)))
graph_price_list = m.find_average(graph_years_list, selected_commodity, district_name)

district_list = m.food_data_frame['market'].tolist()
commodity_list = m.food_data_frame['commodity'].tolist()
date_list = m.food_data_frame['year'].tolist()
