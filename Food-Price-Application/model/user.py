from model.network.jsn_drop_service import jsnDrop
from datetime import datetime
import pandas as pd

class User(object):

    # Constant variables linked to user
    current_user = None
    current_pass = None
    current_status = None
    current_screen = None
    chat_list = []
    chat_thread = None
    stop_thread = False
    this_user_manager = None
    thread_lock = False
    jsn_tok = "6c9cae56-ccbd-45ad-b765-87e28acb57cd"
    latest_time = None


    # Timestamp function 
    def now_time_stamp(self):
        time_now = datetime.now()
        time_now.timestamp()
        return time_now.timestamp()
 

    # Initialize user class
    def __init__(self) -> None:
        super().__init__()

        self.jsnDrop = jsnDrop(User.jsn_tok,"https://newsimland.com/~todd/JSON")

        # SCHEMA Make sure the tables are  CREATED - jsnDrop does not wipe an existing table if it is recreated
        result = self.jsnDrop.create("tblUser",{"PersonID PK":"A_LOOONG_NAME"+('X'*50),
                                                "Password":"A_LOOONG_PASSWORD"+('X'*50),
                                                "Status":"STATUS_STRING"})

        result = self.jsnDrop.create("tblChat",{"Time PK": self.now_time_stamp(),
                                                "PersonID":"A_LOOONG_NAME"+('X'*50),
                                                "DESNumber":"A_LOOONG_DES_ID"+('X'*50),
                                                "Chat":"A_LOONG____CHAT_ENTRY"+('X'*255)
                                                })

        result = self.jsnDrop.create("tblData",{"ID PK AUTO ": 190182,
                                                "date": 10000,
                                                "market": "Long_Region_Name"+('X'*100),
                                                "commodity": "A_long_list",
                                                "usdprice": 1234567890})
        User.this_user_manager = self


    # Function to handle registration of user 
    def register(self, user_id, password):
        api_result = self.jsnDrop.select("tblUser",f"PersonID = '{user_id}'") 

        if( "DATA_ERROR" in self.jsnDrop.jsnStatus): 

            result = self.jsnDrop.store("tblUser",[{'PersonID':user_id,'Password':password,'Status':'Registered'}])
            User.currentUser = user_id
            User.current_status = 'Logged Out'

            result = "Registration Success"
        else:
            result = "User Already Exists"

        return result

    def login(self, user_id, password):
        result = None
        api_result = self.jsnDrop.select("tblUser",f"PersonID = '{user_id}' AND Password = '{password}'") 

        if( "DATA_ERROR" in self.jsnDrop.jsnStatus): 
            result = "Login Fail"
            User.current_status = "Logged Out"
            User.current_user = None
        else:
            User.current_status = "Logged In"
            User.current_pass = password

            api_result = self.jsnDrop.store("tblUser",[{"PersonID":user_id,"Password":password,"Status":"Logged In"}])
            result = "Login Success"

        return result



    def set_current_DES(self, DESScreen):
        result = None
        if User.current_status == "Logged In":
            User.current_screen = DESScreen
            result = "Set Screen"
        else:
            result = "Log in to set the current screen"
        return result


    def chat(self,message):
        result = None
        if User.current_status != "Logged In":
            result = "You must be logged in to chat"
        elif User.current_screen == None:
            result = "Chat not sent. A current screen must be set before sending chat"
        else: 
            user_id = User.current_user
            des_screen = User.current_screen
            api_result = self.jsnDrop.store("tblChat",[{'Time': self.now_time_stamp(),
                                                        'PersonID':user_id,
                                                        'DESNumber':f'{des_screen}',
                                                        'Chat':message
                                                        }])
            if "ERROR" in api_result :
                result = self.jsnDrop.jsnStatus
            else:
                result = "Chat sent"

        return result

    def get_chat(self):
         result = None

         if User.current_status == "Logged In":
            des_screen = User.current_screen  
            if not(des_screen is None):
                api_result = self.jsnDrop.select("tblChat",f"DESNumber = '{des_screen}'")
                if not ('DATA_ERROR' in api_result) :
                    User.chat_list = self.jsnDrop.jsnResult
                    result = User.chat_list

         return result
         
    def logout(self):
        result = "Must be 'Logged In' to 'LogOut' "
        if User.current_status == "Logged In":
            api_result = self.jsnDrop.store("tblUser",[{"PersonID": User.current_user,
                                                        "Password": User.current_pass,
                                                        "Status":"Logged Out"}])
            if not("ERROR" in api_result):
                User.current_status = "Logged Out"
                result = "Logged Out"
            else:
                result = self.jsnDrop.jsnStatus

        return result
    
    def data_populate(self):
        
        # Check user is logged in 
        if User.current_status == "Logged In":

            # Read the data 
            data = pd.read_csv("Food-Price-Application\data\wfp_food_prices_ukr.csv")
            df = pd.DataFrame(data)

            # Store data from dataframe in jsonDrop 
            for row in df.itertuples():
                api_result = self.jsnDrop.store("tblData",[{
                                                            "date":row.date,
                                                            "market":row.market,
                                                            "commodity":row.commodity,
                                                            "usdprice":row.usdprice}])     
    
            if not("ERROR" in api_result):
                User.current_status = "Logged Out"
                
        
    def dropDatabase(self):
        result = self.jsnDrop.drop("tblChat")
        result = self.jsnDrop.drop("tblUser")
        result = self.jsnDrop.drop("tblData")
        
        
    def upload_database(self):
        result = self.jsnDrop.upload("tblUser")
        result = self.jsnDrop.upload("tblChat")
        result = self.jsnDrop.upload("tblData")

