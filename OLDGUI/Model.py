import Common as com

def generate_layout():
    """
    This function works as a state machine which returns a different object of "layout" for creating a screen based on the value of "window_flag",
    this allows the application to 're-use' layouts 
    """
    if com.window_flag == 0:
        layout = [
                    [com.sg.Text("Hello, welcome to the Ukrainian food price tracking application")],
                    [com.sg.Text("Please enter your login details")],
                    [com.sg.Text('Username'), com.sg.InputText(size=(20,1))],
                    [com.sg.Text('Password'), com.sg.InputText(size=(20,1), password_char="*")],
                    [com.sg.Submit(button_text="Login"), com.sg.Cancel(button_text="Exit")]
                ]
    elif com.window_flag == 1:        
        MainScreenColumn1 = [
                                [com.sg.Text("Region")],
                                [com.sg.Combo(generate_districts(),default_value="Kyiv",key="district",size=(30,1))],
                                [com.sg.Text("Beginning date")],
                                [com.sg.Combo(generate_dates(),default_value="2014",size=(30,1), key='begin')],
                                [com.sg.Text("Ending date")],
                                [com.sg.Combo(generate_dates(),default_value="2022",size=(30,1), key='end')],
                                [com.sg.Text("Currency")],
                                [com.sg.Combo(["NZD","USD","EUR","JPY","GBP","AUD","CAD","CHF","CNY","HKD","SEK","KRW","SGD","NOK","MXN","INR","RUB","ZAR","TRY","BRL","TWD","DKK","PLN","THB","IDR","HUF","CZK","ILS","CLP","PHP","AED","COP","SAR","MYR","RON"],default_value='NZD',size=(30,1))],
                                [com.sg.Text("Select foods below to display")],
                                [com.sg.Listbox(values=generate_food(), select_mode="multiple", key="food", size=(30,10))],
                                [com.sg.Button("Change graph")],
                                [com.sg.Button("Display region")]
                            ]
        MainScreenColumn2 = [   
                                # Graph goes here 
                                [com.sg.Canvas(size=(500, 300), key=("-CANVAS-"))]
                            ]
        layout = [
                                [com.sg.Column(MainScreenColumn1, element_justification='l'), com.sg.Column(MainScreenColumn2, element_justification='c')]
                            ]
    elif com.window_flag == 2:  
        layout = [ 
                                [com.sg.Button("Exit to main")],
                                [com.sg.Image(filename=f'map-pics\{com.district_name}.png')]
                            ]

    return layout

def generate_districts():
    """
    This function is designed to generate the available districts to view statistics for and return these
    districts in a list of values to be displayed in a combo box
    """
    # Drop duplicate district names 
    res = list(set(com.district_list))

    # Remove some values I won't be using 
    res.remove("Kyiv city")
    res.remove("Kirovohrad")
    res.remove("m. Sevastopol")

    return res

def generate_food():
    """
    This function is designed to generate a list of food items to be chosen from, from a dataframe to be displayed in a listbox 
    """
    # Drop duplicate district names 
    res = list(set(com.commodity_list))

    return res

def generate_dates():
    """
    This function is designed to return a list of years 
    """
    res = list(set(com.date_list))
    res.sort()
    return res

def find_average(year, food):
    """
    Function designed to return the average price of a food item for a year 
    """
    # Query the CSV file and retrieve the lists of commodities prices based on the year passed to this function 
    commodity_list_local = com.food_data_frame.query(f'year == {year}')['commodity'].tolist()
    price_list_local = com.food_data_frame.query(f'year == {year}')['price'].tolist()

    # Bring the values of both lists together into a list of arrays 
    zipped = list(zip(commodity_list_local , price_list_local))

    # Create a list of the values correlating with the food/commodity passed to the function
    food_item_list = [i for i in zipped if i[0] == food]

    # Find the average of the sum of the values stored in the food item list for that particular food 
    if len(food_item_list) > 0:
        avg = sum(com.Decimal(n[1]) for n in food_item_list) / len(food_item_list)
    else:
        avg = 0

    return round(avg, 2)