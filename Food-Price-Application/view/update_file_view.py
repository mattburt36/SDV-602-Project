import sys

sys.dont_write_bytecode = True
import PySimpleGUI as sg
import controller.Upload.get_target as get_target_csv
import controller.Upload.get_upload_file as get_upload_csv
import controller.Upload.merge_csv as merge_csv
import controller.DES.exit_button as exit_button

class UpdateView(object) :
    
    def __init__(self):
        
        self.window = None
        self.layout = []
        self.components = {"has_components":False}
        self.controls = []
        self.target_file_path = ""
        self.upload_file_path = ""
        self.explorer_view = None
        self.explorer_values = None


    def update_component_text(self,component_name, text):
        if component_name in self.components:
            self.components[component_name].update(text)


    def update_upload_file(self,text):
        self.upload_file_path = text
        self.update_component_text('upload_data_file_name',text)


    def update_target_file(self,text):
        self.target_file_path = text
        self.update_component_text('target_data_file_name',text)


    def layout_screen(self):
        # Define theme 
        sg.theme('DarkTeal10')
        figure_w, figure_h = 650, 650

        # Define components 
        self.components['upload_data_file_name'] = sg.Text('No data')
        self.components['select_upload_file'] = sg.Button(button_text="Select Upload CSV",size=(10, 2))
        self.controls += [get_upload_csv.accept]

        self.components['target_data_file_name'] = sg.Text('No data')
        self.components['select_target_file'] = sg.Button(button_text="Select Target CSV",size=(10, 2))
        self.controls += [get_target_csv.accept]

        
        self.components['merge'] = sg.Button(button_text="Merge CSV",size=(10, 2))
        self.controls += [merge_csv.accept]

        self.components['exit_button'] = sg.Exit(size=(5, 2))        
        self.controls += [exit_button.accept]

        row_buttons = [ 
                        self.components['select_upload_file'],
                        self.components['select_target_file'],
                        self.components['merge'], 
                        self.components['exit_button'] 
                      ]

        # Define layout 
        self.layout = [
                        [self.components['header']],
                        [sg.Text('Upload File is:'),self.components['upload_data_file_name'] ], 
                        [sg.Text('Target File is: '),self.components['target_data_file_name']], 
                        row_buttons
                      ]


    def create(self):

        # Create form 
        if self.layout:
            self.window =sg.Window('Upload data', self.layout, grab_anywhere=False, finalize=True)
  

    def await_input(self):

        if self.window:
            run = True
            
            while run:
                event, values = self.window.read()
                for accept_control in self.controls:
                    run = accept_control(event,values,{'view':self})
            self.window.close()