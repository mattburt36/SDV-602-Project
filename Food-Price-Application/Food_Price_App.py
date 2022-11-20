"""
Please Initialize the application from this file, refer to the "README.md" File for more information on this application 
"""

import sys
sys.dont_write_bytecode = True
from view.login_view import LoginView

if __name__ == "__main__":
    """
    Initialize code 
    """

    login_view = LoginView()
    login_view.layout_screen()
    login_view.create()
    login_view.await_input()

    pass
