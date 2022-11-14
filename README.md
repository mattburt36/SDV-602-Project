Ukrainian food price application
Designer: Matthew Burton 
Begin Date: 01/08/2022
End Date: N/A

This is my application for NMIT Semester 2 of 2022, SDV602 class tutored by Todd Cochrane. 
The intention of this application is to track the prices of food in the war torn country of the Ukraine. I do not personally agree with any form of war, I am just studying the effects on the people in different areas of the Ukraine that are affected by the war. 

This application may take a dataset of the Ukraine and produce results to be displayed graphically on the prices of items, in the future I aim to make this application have the ability to adapt to different countries and different options datasets allow. 

This application's current state is a test state, accepting a dataset which produces results graphically on the prices of foods selected from a list 

The application uses the libraries:
    - PySimpleGUI   (For layout and presentation of windows in graphical user interface)
    - Matplotlib    (For layout of graphs to insert into the windows generated by PySimpleGUI)
    - Tkinter       (To generate message boxes to display errors or unexpected results)
    - Pandas        (To manipulate and analyse data)

This application follows the MVC pattern: 

    Model: manages the data and defines rules and behaviors. It represents the business logic of the application. The data can be stored in the Model itself or in a database (only the Model has access to the database).

    View: presents the data to the user. A View can be any kind of output representation: a HTML page, a chart, a table, or even a simple text output. A View should never call its own methods; only a Controller should do it.

    Controller: accepts user’s inputs and delegates data representation to a View and data handling to a Model.

Enjoy!