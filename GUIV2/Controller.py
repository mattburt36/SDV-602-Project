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
        # The system is in the login screen state, showing the first screen      
        if c.window_flag == 0:
            if event == "Exit":
                break
            if event == "Login":
                # check credentials, close last window, open the main screen
                # print(com.date_list)
                c.window_flag = 2 
                # close previous window 
                window.close()
                window = v.create_window()

        #---------------------------------------------------------------------------------------------
        #   - Registration window:  window_flag == 1
        #   TODO ADD registration window here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #---------------------------------------------------------------------------------------------
        #   - Graph window:         window_flag == 2
                # The system is in the main screen state, showing the secondarily generated screen  
        elif c.window_flag == 2:
            if event == "Change graph":  
                # Switch the value of the graph in a simple state machine 
                if c.graph_flag == 0:
                    c.graph_flag = 1
                elif c.graph_flag == 1:
                    c.graph_flag = 0

            if event == "Display region":
                # Show map screen 
                # Keep the main screen open but not interactive
                # Set the district_name variable to be equal to the value of the combo box with the key "district" so that the correct district image may be produced 
                c.district_name = values['district']
                c.window_flag = 3
                window = v.create_window()

        #---------------------------------------------------------------------------------------------
        #   - Map window:           window_flag == 3
                # The system is in the map screen state, showing the thirdly generated screen  
        elif c.window_flag == 3:
            if event == "Exit to main" or event == c.sg.WIN_CLOSED():
                # Show the main screen
                c.window_flag = 2
                window.close()
                window = v.create_window()

    #-------------------------------------------------------------------------------------------------
    # Default to no window open once all conditions are satisfied 
    window.close()