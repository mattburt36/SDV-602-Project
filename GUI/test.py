from decimal import *
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Read the data from the CSV folder of "Ukrainian_food" and store in a variable that will not be altered 
food_data_frame = pd.read_csv('Ukrainian_food.csv', low_memory=False)
food_data_frame.drop(0, axis=0, inplace=True)

food_data_frame['date'] = pd.to_datetime(food_data_frame['date'])
food_data_frame['year'] = food_data_frame['date'].dt.year

district_list = food_data_frame['market'].tolist()

commodity_list = food_data_frame['commodity'].tolist()
year_list = food_data_frame['year'].to_list()
price_list = food_data_frame['price'].to_list()

def find_average(year, food, market):
    """
    Function designed to return the average price of a food item for a year 
    """
    # Query the CSV file and retrieve the lists of commodities prices based on the year passed to this function 
    commodity_list_local = food_data_frame.query(f'year == {year}')['commodity'].tolist()
    price_list_local = food_data_frame.query(f'year == {year}')['price'].tolist()
    market_list_local = food_data_frame.query(f'year == {year}')['market'].tolist()

    # Bring the values of both lists together into a list of arrays 
    zipped = list(zip(commodity_list_local , price_list_local, market_list_local))

    # Create a list of the values correlating with the food/commodity passed to the function
    food_item_list = [i for i in zipped if i[0] == food and i[2] == market]

    # Find the average of the sum of the values stored in the food item list for that particular food 
    if len(food_item_list) > 0:
        avg = sum(Decimal(n[1]) for n in food_item_list) / len(food_item_list)
    else:
        avg = 0

    return round(avg, 2)

# Sort list of foods, years and districts 
years = list(set(year_list))
years.sort()
foods = list(set(commodity_list))
foods.sort()
places = list(set(district_list))
places.sort()

# Iterate through each year in stored list 
for y in years:
    # Print this value 
    print(y)
    # Iterate through each place in stored list 
    for j in places:
        # Print this value 
        print(j)
        # Iterate through each food/commodity in stored list 
        for i in foods:
            # Print the value of the result of the function being passed the year, place and food 
            print(i, " : ", find_average(y, i, j))

  
def create_plot(x, y):
    """
    Function to plot graph values, switch between types of graph to be plotted 
    """
    # Dispose any past graphs that were plotted 
    plt.cla()
    
    plt.plot(x, y, color="blue", marker="o")

    plt.title("Food prices")
    plt.xlabel("Year")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.show()

    return plt.gcf()
