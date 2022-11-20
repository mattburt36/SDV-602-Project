import PySimpleGUI as Psg
import controller.DES.exit_button as exit
import controller.User.login_button as login
import controller.User.registration_button as registration

# Login screen class, first view of the application for user to enter details, can either go to main DES screen or registration screen 
class LoginView(object):

    # Init login screen class 
    def __init__(self):

        self.window = None
        self.layout = []
        self.components = {"has_components": False}
        self.controls = []

    def layout_screen(self):

        # Choose theme for login screen 
        Psg.theme('DarkTeal10')

        # Create components of login screen 
        self.components['User'] = Psg.InputText('', key='User')
        self.components['Password'] = Psg.InputText('', key='Password', password_char='*')

        self.components['Login'] = Psg.Button(button_text="Login", size=(8, 2))
        self.controls += [login.accept]

        self.components['RegisterWindow'] = Psg.Button(button_text="Register", size=(8, 2))
        self.controls += [registration.accept]

        self.components['exit_button'] = Psg.Exit(size=(8, 2))
        self.controls += [exit.accept]

        # Define buttons
        row_buttons = [
                        self.components['Login'],
                        self.components['RegisterWindow'],
                        self.components['exit_button']
                      ]

        # Define layout
        self.layout = [
                        [Psg.Text('User Name:'), self.components['User']],
                        [Psg.Text('Password : '), self.components['Password']],
                        row_buttons
                      ]

    def create(self):

        # create login form
        if self.layout:
            self.window = Psg.Window('Sign in', self.layout, grab_anywhere=False, finalize=True, resizable=True, size=(270,110))

    def await_input(self):

        # await for user input
        if self.window:
            run = True

            while run:
                event, values = self.window.read()
                for accept_control in self.controls:
                    run = accept_control(event, values, {'view': self})
            self.window.close()
