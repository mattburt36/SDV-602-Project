"""
View Module
"""

import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    """
    View class
    """
    PAD = 10

    def __init__(self, controller):
        """
        Constructor
        """
        # initiliase superclass
        super().__init__()  
        # Title 
        self.title('PyCalc1.0')

        self.controller = controller

        #Set the value of a string entered in a box to a variable 
        self.value_var = tk.StringVar()

        self._make_main_frame()
        self._make_entry()

    def main(self):
        self.mainloop()


    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        ent = ttk.Entry(self.main_frm, justify='right',textvariable=self.value_var)
        ent.pack()