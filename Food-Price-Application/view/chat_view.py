import PySimpleGUI as sg
import controller.DES.exit_button as exit_button
import controller.User.chat_button as chat_button
from model.user import User
from threading import Thread
import threading
import signal

class ChatView(object):

    def __init__(self):
        
        self.window = None
        self.layout = []
        self.components = {"has_components":False}
        self.controls = []
        self.values = None
        # The following will only work if we have logged in!
        self.JsnDrop = User.this_user_manager.jsnDrop
        # Thread for chat
        self.chat_count = 0
        self.exit_event = threading.Event()
        signal.signal(signal.SIGINT, self.signal_handler)


    def signal_handler(self,signum, frame):
        self.exit_event.set()   

    def set_up_chat_thread(self):
        User.chat_thread = Thread(target=self.chat_display_update,args=(User,))
        User.chat_thread.setDaemon(True)
        User.stop_thread = False
        User.chat_thread.start()


    def chat_display_update(self, User):
        print("Thread chat")
    
        # Check there is a window before sending an event to it
        if self.window:
            self.chat_count += 1
            # Go to network service to get the Chats
            result = self.JsnDrop.select("tblChat", f"DESNumber = '{User.current_screen}'")

            if result != "Data error. Nothing selected from tblChat":
                messages = ""
                # Sort the result records by the Time field
                sorted_chats = sorted(result,key = lambda i : i['Time'] )

                for record in sorted_chats:
                    new_display = ""
                    if not (User.latest_time is None):

                        if record['Time'] > User.latest_time:
                            new_display = f"{record['PersonID']}[{record['Chat']}]\n"

                    else: 
                        new_display = f"{record['PersonID']}[{record['Chat']}]\n"
                    messages += new_display

                User.chat_count = [messages]

                # Keep number of messages down to 5
                if len(User.chat_count) > 5:
                    User.chat_count = User.chat_count[:-5]
                
                # Makes a string of messages to update the display
                Update_Messages = ""
                for messages in User.chat_count:
                    Update_Messages+= messages
                
                # Send the Event back to the window if we have n't already stopped
                if not User.stop_thread:

                    # Time stamp the latest record
                    latest_record = sorted_chats[:-1][0]
                    User.latest_time = latest_record['Time']

                    # Send the event back to the window
                    self.window.write_event_value('-CHATTHREAD-', Update_Messages)
        # The Thread stops - no loop - when the event is caught by the Window it starts a new long task

                                                
    def layout_screen(self):

        # Define theme 
        sg.theme('DarkTeal10')
        
        #Define components
        self.components['ChatDisplay'] = sg.Multiline('CHATTY',autoscroll=True,disabled=True, key='ChatDisplay',size=(70,25))
        self.components['Message'] =sg.InputText('Type a message', key='Message',size=(40,100))
        self.components['Send'] = sg.Button('Send', key='Send', size=(10,2))
        self.controls += [chat_button.accept]


        self.components['exit_button'] = sg.Exit(size=(5, 2))        
        self.controls += [exit_button.accept]

        row_buttons = [ 
                        self.components['exit_button'] 
                      ]

        # Define layout 
        self.layout = [
                        
                        [self.components['ChatDisplay'] ], 
                        [self.components['Message']],
                        [self.components['Send']], 
                        row_buttons
                      ]


    def create(self):
        if self.layout:
            self.window =sg.Window('Chat', self.layout, grab_anywhere=False, finalize=True, resizable=True)
            # Need a window before chat
            self.set_up_chat_thread()
  
  
    def await_input(self):
        if self.window:
            run = True
            
            while run:
                event, values = self.window.read()

                if event == "Exit":
                    User.stop_thread = True
                    
                elif event == "-CHATTHREAD-" and not User.stop_thread:
                    # Lock until the Window is updated
                    User.stop_thread = True

                    self.window['ChatDisplay'].Update(values[event])
                    # This should always be True here
                    if User.stop_thread:
                        # Unlock so we can start another long task thread
                        User.stop_thread = False
                        # Start another long task thread
                        self.set_up_chat_thread()


                for accept_control in self.controls:
                    run = accept_control(event,values,{'view':self})
            self.window.close()
        