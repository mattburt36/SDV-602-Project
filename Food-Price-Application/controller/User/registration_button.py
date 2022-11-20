"""
Register Window controller
"""
import sys
sys.dont_write_bytecode = True

def accept( event, values, state):

    from view.registration_view import RegistrationView

    run = True
    if event == "Register":   
        register_view = RegistrationView()
        register_view.layout_screen()
        register_view.create()
        register_view.await_input()
    else:
        run = True

    return run