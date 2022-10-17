import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from decimal import *

theme = 'DarkTeal10'

# Set the theme for the application 
sg.theme(theme)

# Set some initial conditions  
graph_flag = 0
window_flag = 0
district_name = 'Kyiv'
selected_commodity = 'Milk'
begin_year = 2014
end_year = 2022
graph_years_list = list(range(begin_year, (end_year + 1)))

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
