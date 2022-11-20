"""
Chat Controller
"""
import sys
from time import sleep
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import view.chat_view as chat_view



def accept( event, values,state):
    
    keep_going = True
    if event == "Send":   
            
        
        # Work with a UserManager object
        from model.user_manager import UserManager
        a_user_manager = UserManager()
        # get user name and password from the "values" or "state"
        message = values['Message']
        #print(f"Got Message = {message}  - just testing")
        
        message_result = a_user_manager.chat(message)
        print(f"Got chat result: {message_result}")
        
        #the_chat_view = state['View']
        #the_chat_view.chat_display_update(message_result, UserManager)
  
        
    else:
        keep_going = True

    return keep_going 

