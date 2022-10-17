"""
This file contains variables and manipulatable data along with functions to complete those manipulations based on the actions completed by the user in the Controller.py file
"""
import Common as c

# Read the data from the CSV folder of "Ukrainian_food" and store in a variable that will not be altered 
food_data_frame = c.pd.read_csv('Ukrainian_food.csv', low_memory=False)
# The following statement is to remove a row of values from the CSV that contian invalid information 
food_data_frame.drop(0, axis=0, inplace=True)

# Retrieve the years from the date column
food_data_frame['date'] = c.pd.to_datetime(food_data_frame['date'])
food_data_frame['year'] = food_data_frame['date'].dt.year

def generate_layout():
    """
    This function works as a state machine which returns a different object of "layout" for creating a screen based on the value of "window_flag",
    this allows the application to 're-use' layouts 
    """
    #----------------------------------------------------------------------------------------------------------------
    # Login window
    if c.window_flag == 0:
        layout = [
                                [c.sg.Text("Hello, welcome to the Ukrainian food price tracking application")],
                                [c.sg.Text("Please enter your login details")],
                                [c.sg.Text('Username'), c.sg.InputText(size=(20,1))],
                                [c.sg.Text('Password'), c.sg.InputText(size=(20,1), password_char="*")],
                                [c.sg.Submit(button_text="Login"), c.sg.Cancel(button_text="Exit")]
                            ]
    #----------------------------------------------------------------------------------------------------------------
    # Graph window
    elif c.window_flag == 2:        
        MainScreenColumn1 = [
                                [c.sg.Text("Region")],
                                [c.sg.Combo(generate_districts(),default_value="Kyiv",key="district",size=(30,1))],
                                [c.sg.Text("Beginning date")],
                                [c.sg.Combo(generate_dates(),default_value="2014",size=(30,1), key='begin')],
                                [c.sg.Text("Ending date")],
                                [c.sg.Combo(generate_dates(),default_value="2022",size=(30,1), key='end')],
                                [c.sg.Text("Currency")],
                                [c.sg.Combo(["NZD","USD","EUR","JPY","GBP","AUD","CAD","CHF","CNY","HKD","SEK","KRW","SGD","NOK","MXN","INR","RUB","ZAR","TRY","BRL","TWD","DKK","PLN","THB","IDR","HUF","CZK","ILS","CLP","PHP","AED","COP","SAR","MYR","RON"],default_value='NZD',key='currency',size=(30,1))],
                                [c.sg.Text("Select foods below to display")],
                                [c.sg.Listbox(values=generate_commodity(), select_mode="single", key="commodity", size=(30,10))],
                                [c.sg.Button("Change graph ")],
                                [c.sg.Button("Display region")],
                                [c.sg.Button("Refresh graph ")]
                            ]
        MainScreenColumn2 = [   
                                # Graph goes here 
                                [c.sg.Canvas(size=(500, 300), key=("-CANVAS-"))]
                            ]
        layout = [
                                [c.sg.Column(MainScreenColumn1, element_justification='l'), c.sg.Column(MainScreenColumn2, element_justification='c')]
                            ]
    #----------------------------------------------------------------------------------------------------------------
    # Map window
    elif c.window_flag == 3:  
        layout = [ 
                                [c.sg.Button("Exit to main")],
                                [c.sg.Image(filename=f'map-pics\{c.district_name}.png')]
                            ]

    return layout

def generate_districts():
    """
    This function is designed to generate a list of districts and remove unwanted values
    """
    # Drop duplicate district names 
    res = list(set(c.district_list))
    res.sort()

    # Remove some values I won't be using 
    res.remove("Kyiv city")
    res.remove("Kirovohrad")
    res.remove("m. Sevastopol")

    return res

def generate_commodity():
    """
    This function is designed to generate a list of food/commodity items 
    """
    # Drop duplicate district names 
    res = list(set(c.commodity_list))

    return res

def generate_dates():
    """
    This function is designed to return a list of years 
    """
    res = list(set(c.date_list))
    res.sort()
    return res

def find_average(year, food, market):
    """
    Function designed to return the average price of a food item for a year 
    """
    res = []
    for index in range(len(year)):
        # Query the CSV file and retrieve the lists of commodities prices based on the year passed to this function 
        commodity_list_local = food_data_frame.query(f'year == {year[index]}')['commodity'].tolist()
        price_list_local = food_data_frame.query(f'year == {year[index]}')['price'].tolist()
        market_list_local = food_data_frame.query(f'year == {year[index]}')['market'].tolist()

        # Bring the values of both lists together into a list of arrays 
        zipped = list(zip(commodity_list_local , price_list_local, market_list_local))

        # Create a list of the values correlating with the food/commodity passed to the function
        food_item_list = [i for i in zipped if i[0] == food and i[2] == market]

        # Find the average of the sum of the values stored in the food item list for that particular food 
        if len(food_item_list) > 0:
            avg = sum(c.Decimal(n[1]) for n in food_item_list) / len(food_item_list)
        else:
            avg = 0

        res.append(int(round(avg,2)))

    return res