"""
Ukrainian food price application
Designer: Matthew Burton 
Begin Date: 01/08/2022
End Date: N/A

This is my application for NMIT Semester 2 of 2022, SDV602 class tutored by Todd Cochrane. 
The intention of this application is to track the prices of food in the war torn country of the Ukraine. I do not personally agree with any form of war, I am just studying the effects
on the people in different areas of the Ukraine that are affected by the war. 

This application may take a dataset of the Ukraine and produce results to be displayed graphically on the prices of items, in the future I aim to make this application have the ability 
to adapt to different countries and different options datasets allow. 

This application's current state is a test state, accepting a dataset which produces results graphically on the prices of foods selected from a list 

The application uses the libraries:
    - PySimpleGUI   (For layout and presentation of windows in graphical user interface)
    - Matplotlib    (For layout of graphs to insert into the windows generated by PySimpleGUI)
    - Tkinter       (To generate message boxes to display errors or unexpected results)
    - Pandas        (To manipulate and analyse data)

I have stored variables in a 'Common' file, this is to clean any mess, reduce the time it takes to change variable values by storing them all in the one place
I have stored manipulatable data in a 'Model' file, this is to keep data organised in a module to be manip[ulated when necessary

Enjoy! 
"""
import Common as com
import View as view

window = view.create_window()

if __name__ == "__main__":

    # Application's main event loop 
    while True:
        event, values = window.read()
        # For any state the machine is in, if the window is closed, exit the application entirely
        if event == com.sg.WIN_CLOSED:
            break
        # The system is in the login screen state, showing the first screen      
        if com.window_flag == 0:
            if event == "Exit":
                break
            if event == "Login":
                # check credentials, close last window, open the main screen
                # print(com.date_list)
                com.window_flag = 1 
                # close previous window 
                window.close()
                window = view.create_window()
                view.draw_graph(window["-CANVAS-"].TKCanvas, view.create_plot(com.default_years, com.test_prices, com.graph_flag))        
        # The system is in the main screen state, showing the secondarily generated screen  
        elif com.window_flag == 1:
            if event == "Change graph":  
                # Switch the value of the graph that is plotted 
                if com.graph_flag == 0:
                    com.graph_flag = 1
                elif com.graph_flag == 1:
                    com.graph_flag = 0
                # TODO make this function refresh the graph canvas rather than close the whole screen 
                # close previous window
                com.plt.cla()
                com.plt.clf()  
                view.draw_graph(window["-CANVAS-"].TKCanvas, view.create_plot(com.default_years, com.test_prices, com.graph_flag))

            if event == "Display region":
                # Show map screen 
                # Keep the main screen open but not interactive
                # Set the district_name variable to be equal to the value of the combo box with the key "district"
                com.district_name = values['district']
                com.window_flag = 2
                window = view.create_window()

        # The system is in the map screen state, showing the thirdly generated screen  
        elif com.window_flag == 2:
            if event == "Exit to main" or event == com.sg.WIN_CLOSED():
                # Show the main screen
                com.window_flag = 1
                window.close()
                window = view.create_window()
                view.draw_graph(window["-CANVAS-"].TKCanvas, view.create_plot(com.test_years, com.test_prices, com.graph_flag))

    # Default state once conditions are satisfied 
    window.close() 