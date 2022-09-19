""" 
File to manage data, the behavior of data and the rules the data should follow
"""
import Common 

# Test data
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
prices = [15, 17, 19, 20, 16, 19, 22, 40, 45]

def generate_layout():
    """
    This function works as a state machine which returns a different object of "layout" for creating a screen based on the value of "window_flag",
    this allows the application to 're-use' layouts 
    """
    if window_flag == 0:
        layout = [
                    [sg.Text("Hello, welcome to the Ukrainian food price tracking application")],
                    [sg.Text("Please enter your login details")],
                    [sg.Text('Username'), sg.InputText(size=(20,1))],
                    [sg.Text('Password'), sg.InputText(size=(20,1), password_char="*")],
                    [sg.Submit(button_text="Login"), sg.Cancel(button_text="Exit")]
                ]
    elif window_flag == 1:        
        MainScreenColumn1 = [
                                [sg.Text("Region")],
                                [sg.Combo(["Kyiv","Dnipropetrovsk","Donetsk","Kharkiv","Kherson","Odesa","Sevastopol","Sumy","Zaporizhzhya"],default_value="Kyiv",size=(30,1))],
                                [sg.Text("Beginning date")],
                                [sg.Combo(["2014","2015","2016","2017","2018","2019","2020","2021","2022"],default_value="2014",size=(30,1))],
                                [sg.Text("Ending date")],
                                [sg.Combo(["2014","2015","2016","2017","2018","2019","2020","2021","2022"],default_value="2022",size=(30,1))],
                                [sg.Text("Currency")],
                                [sg.Combo(["NZD","USD","EUR","JPY","GBP","AUD","CAD","CHF","CNY","HKD","SEK","KRW","SGD","NOK","MXN","INR","RUB","ZAR","TRY","BRL","TWD","DKK","PLN","THB","IDR","HUF","CZK","ILS","CLP","PHP","AED","COP","SAR","MYR","RON"],default_value='NZD',size=(30,1))],
                                [sg.Text("Select foods below to display")],
                                [sg.Listbox(values=["Fuel(petrol)","Milk","Potatoes","Rice","Onions","Cabbage","Carrots","Beetroot","Apples","Sugar","Beef","Chicken","Fish","Pork","Eggs","Flour","Oil(sunflower)","Anti-biotics"], select_mode="multiple", key="food", size=(30,10))],
                                [sg.Button("Change graph")],
                                [sg.Button("Display region")]
                            ]
        MainScreenColumn2 = [   
                                # Graph goes here 
                                [sg.Canvas(size=(500, 300), key=("-CANVAS-"))]
                            ]
        layout = [
                                [sg.Column(MainScreenColumn1, element_justification='l'), sg.Column(MainScreenColumn2, element_justification='c')]
                            ]
    elif window_flag == 2:  
        layout = [ 
                                [sg.Button("Exit to main")],
                                [sg.Image(filename="Ukraine_map.png")]
                            ]

    return layout