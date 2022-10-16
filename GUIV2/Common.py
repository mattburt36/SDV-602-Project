"""
This file houses variables and libraries for the main GUI, it is to be accessible and visible by each other module  
"""
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from decimal import *

# Set some initial conditions
sg.theme('DarkTeal10')  
graph_flag = 0
window_flag = 0
district_name = 'Kyiv'

# Read the data from the CSV folder of "Ukrainian_food" and store in a variable that will not be altered 
food_data_frame = pd.read_csv('Ukrainian_food.csv', low_memory=False)
# The following statement is to remove a row of values from the CSV that contian invalid information 
food_data_frame.drop(0, axis=0, inplace=True)

# Retrieve the years from the date column
food_data_frame['date'] = pd.to_datetime(food_data_frame['date'])
food_data_frame['year'] = food_data_frame['date'].dt.year

district_list = food_data_frame['market'].tolist()
commodity_list = food_data_frame['commodity'].tolist()
date_list = food_data_frame['year'].tolist()