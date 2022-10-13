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

def find_average(year, food):

    commodity_list_local = food_data_frame.query(f'year == {year}')['commodity'].tolist()
    price_list_local = food_data_frame.query(f'year == {year}')['price'].tolist()
    # Bring the values of both lists together into a list of arrays 
    zipped = list(zip(commodity_list_local , price_list_local))

    res = [item for item in zipped if item[0] == food]

    average = sum(float(n[1]) for n in res) / len(res)

    return round(average, 2)

print(find_average(2016,'Milk'))

"""
def create_plot(x, y):

    Function to plot graph values, switch between types of graph to be plotted 

    # Dispose any past graphs that were plotted 
    plt.cla()
    
    plt.plot(x, y, color="blue", marker="o")

    plt.title("Food prices")
    plt.xlabel("Year")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.show()

    return plt.gcf()

create_plot()
"""
