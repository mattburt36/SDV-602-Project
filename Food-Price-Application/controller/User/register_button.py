"""
Register controller
"""
import sys
sys.dont_write_bytecode = True


def accept( event, values, state):
    
    run = True
    if event == "Register":   

        # Work with a User object
        from model.user import User
        a_user_manager = User()

        # get user name and password from the "values" or "state"
        user_name = values['User']
        password = values['Password']

        register_result = a_user_manager.register(user_name,password)
        print(f"REGISTRATION RESULT = {register_result}")

    else:
        run = True

    return run