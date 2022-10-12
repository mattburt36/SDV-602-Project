import dis
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
                                [com.sg.Combo(["Cherkasy","Chernihiv","Chernivtsi","Dnipro","Donetsk","Ivano-Frankivsk","Kharkiv","Kherson","Khmelnytskyi","Kropyvnytskyi","Kyiv","Luhansk","Lutsk","Lviv","Mykolaiv","Odesa","Poltava","Rivne","Simferopol","Sumy","Ternopil","Uzhhorod","Vinnytsia","Zaporizhzhia","Zhytomyr"],default_value="Kyiv",key="district",size=(30,1))],
                                [com.sg.Text("Beginning date")],
                                [com.sg.Combo(["2014","2015","2016","2017","2018","2019","2020","2021","2022"],default_value="2014",size=(30,1))],
                                [com.sg.Text("Ending date")],
                                [com.sg.Combo(["2014","2015","2016","2017","2018","2019","2020","2021","2022"],default_value="2022",size=(30,1))],
                                [com.sg.Text("Currency")],
                                [com.sg.Combo(["NZD","USD","EUR","JPY","GBP","AUD","CAD","CHF","CNY","HKD","SEK","KRW","SGD","NOK","MXN","INR","RUB","ZAR","TRY","BRL","TWD","DKK","PLN","THB","IDR","HUF","CZK","ILS","CLP","PHP","AED","COP","SAR","MYR","RON"],default_value='NZD',size=(30,1))],
                                [com.sg.Text("Select foods below to display")],
                                [com.sg.Listbox(values=["Fuel(petrol)","Milk","Potatoes","Rice","Onions","Cabbage","Carrots","Beetroot","Apples","Sugar","Beef","Chicken","Fish","Pork","Eggs","Flour","Oil(sunflower)","Anti-biotics"], select_mode="multiple", key="food", size=(30,10))],
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

def generate_districts(df):
    """
    This function is designed to generate the available districts to view statistics for and return these
    districts in a list of values to be displayed in a combo box
    """
    # Init to empty list 
    # Drop duplicate district names 
    district_list = df['market'].tolist()
    res = list(set(district_list))

    # Remove some values I won't be using 
    res.remove("#loc+market+name")
    res.remove("Kyiv city")
    return res