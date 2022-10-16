"""
This file houses the controls the user will utilise when the application is being executed (the main for loop for the GUI)\
This file has scope of the View.py file to 'watch' what users are doing with what information 

This file is where the code execution begins/ends, start execution here 
"""
import Common as c 
import View as v

#-----------------------------------------------------------------------------------------------------
# Instantiate the window 
window = v.create_window()

#-----------------------------------------------------------------------------------------------------
# Initialize the main loop
if __name__ == "__main__":
    while True: 
        #---------------------------------------------------------------------------------------------
        # Assign the events variable to window.read() to track event and value changes on the GUI 
        event, values = window.read()

        #---------------------------------------------------------------------------------------------
        # Regardless of state, given that the form is closed, exit the main loop and application 
        if event == c.sg.WIN_CLOSED:
            break

        #---------------------------------------------------------------------------------------------
        # Run a constant update on the graph being displayed, based on changes of any kind in the GUI

        #---------------------------------------------------------------------------------------------
        # Run state machine check on window_flag to control different events 
        #   - Login window:         window_flag == 0 
        #   - Registration window:  window_flag == 1
        #   - Graph window:         window_flag == 2
        #   - Map window:           window_flag == 3
        
    #-------------------------------------------------------------------------------------------------
    # Default to no window open once all conditions are satisfied 
    window.close()