"""
Login controller
"""
import sys
sys.dont_write_bytecode = True
from view.DES_view import DES_View

def accept( event, values, state):
    
    # Set variable to track 
    run = True

    # Login button has been pressed
    if event == "Login":   
        # Work with a User object
        from model.user import User
        a_user_manager = User()
        
        # get user name and password from the "values"
        user_name = values['User']
        password = values['Password']

        login_result = a_user_manager.login(user_name,password)

        #Populate data call
        a_user_manager.data_populate()

        if login_result == "Login Success":
            User.current_screen = "DES"
            des_view = DES_View()
            des_view.set_up_layout()
            des_view.render()
            des_view.accept_input()

    else:
        run = True

    return run