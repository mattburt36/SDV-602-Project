import PySimpleGUI as Psg
import controller.DES.exit_button as exit_button
import controller.User.register_button as register_button

class RegistrationView(object):


    def __init__(self):
        
        self.window = None
        self.layout = []
        self.components = {"has_components":False}
        self.controls = []


    def layout_screen(self):

        Psg.theme('Topanga')
        
        # Create components for registration screen 
        self.components['User'] = Psg.InputText('', key='User')
        self.components['Password'] = Psg.InputText('', key='Password', password_char='*')

        self.components['Register'] = Psg.Button(button_text="Register", size=(8, 2))
        self.controls += [register_button.accept]

        self.components['exit_button'] = Psg.Exit(size=(8, 2))        
        self.controls += [exit_button.accept]

        # Define buttons
        row_buttons = [ 
                        self.components['Register'], 
                        self.components['exit_button'] 
                      ]

        # Define layout 
        self.layout = [
                        [Psg.Text('Please enter user details to register')],
                        [Psg.Text('User Name:'),self.components['User']], 
                        [Psg.Text('Password : '),self.components['Password']], 
                        row_buttons
                      ]


    def create(self):
        # create registration form 
        if self.layout:
            self.window = Psg.Window('Register', self.layout, finalize=True, no_titlebar=True, size=(250, 120))
  
    def await_input(self):
        # await for user input
        if self.window:
            run = True
            
            while run:
                event, values = self.window.read()
                for accept_control in self.controls:
                    run = accept_control(event,values,{'view':self})
            self.window.close()
