"""
Initialise execution from this file 
"""
import data.common as com
import view.create_plot as plt
import view.create_window as wndw
import view.draw_graph as grph

window = wndw.create_window()

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
                window = wndw.create_window()
                grph.draw_graph(window["-CANVAS-"].TKCanvas, plt.create_plot(com.graph_years_list, com.graph_flag))

        # The system is in the main screen state, showing the secondarily generated screen  
        elif com.window_flag == 1:
            if event == "Change graph ":  
                # Switch the value of the graph that is plotted 
                if com.graph_flag == 0:
                    com.graph_flag = 1
                elif com.graph_flag == 1:
                    com.graph_flag = 0
                    
                # TODO make this function refresh the graph canvas rather than close the whole screen 
                # close previous window
                # Assign a variable the commodity chosen 
                com.district_name = values['district']
                com.selected_commodity = values['food']

                # Produce the other graph with the selected items 
                com.begin_year = values['begin']
                com.end_year = values['end']

                # Refresh
                window.close()
                window = wndw.create_window()
                grph.draw_graph(window["-CANVAS-"].TKCanvas, plt.create_plot(com.graph_years_list, com.graph_flag))

            if event == "Display region":
                # Show map screen 
                # Keep the main screen open but not interactive
                # Set the district_name variable to be equal to the value of the combo box with the key "district"
                com.district_name = values['district']
                com.window_flag = 2
                window = wndw.create_window()

            if event == "Refresh graph ":
                com.district_name = values['district']
                com.selected_commodity = values['food']

                # Produce the other graph with the selected items 
                com.begin_year = values['begin']
                com.end_year = values['end']

                # Refresh
                window.close()
                window = wndw.create_window()
                grph.draw_graph(window["-CANVAS-"].TKCanvas, plt.create_plot(com.graph_years_list, com.graph_flag))

        # The system is in the map screen state, showing the thirdly generated screen  
        elif com.window_flag == 2:
            if event == "Exit to main":
                # Show the main screen
                com.window_flag = 1
                window.close()
                window = wndw.create_window()
                grph.draw_graph(window["-CANVAS-"].TKCanvas, plt.create_plot(com.graph_years_list, com.graph_flag))

    # Default state once conditions are satisfied 
    window.close() 
