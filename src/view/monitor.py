import tkinter as tk

from .screen import Screen
from .controls import Controls
from .connection import Connection
from .messages import Messages

from tkinter.ttk import Button

class Monitor(tk.Tk):
    
    """
        Class to view a monitor to show frames
    """
    def __init__(self, controller):
        super().__init__()
        
        self.__width__ = 560
        self.__height__ = 370
        self.__title__ = 'Node'
        self.__resizable__ = False
        self.__controller__ = controller # controller
        
        self.setup()
        self.setup_screen()
        self.setup_controls(self.__controller__.get_socket_controller())
        self.setup_connection(self.__controller__.get_socket_controller())
        self.setup_messages()
        self.setup_button_exit()
                
    def setup(self):
        self.title(self.__title__)
        self.geometry(f'{self.__width__}x{self.__height__}')
        self.resizable(self.__resizable__, self.__resizable__)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
    def setup_screen(self):
        self.__screen__ = Screen(self)
        self.__screen__.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5, sticky='news')
        # __screen__.pack(side='left', fill='x', expand=1, padx=5, pady=5)

    def setup_controls(self, controls_controller):
        self.__controls__ = Controls(self, controls_controller)
        self.__controls__.grid(row=2, column=0, rowspan=2, columnspan=2, padx=5, pady=5, sticky='new')
        # __source__.pack(side='top', fill='x', expand=1, padx=5, pady=5)

    def setup_connection(self, socket_controller):
        self.__connection__ = Connection(self, socket_controller)
        self.__connection__.grid(row=0, column=2, rowspan=1,
                            columnspan=2, pady=5, padx=5, sticky='new')
        # __options__.pack(side='top', fill='x', expand=1, padx=5, pady=5)

    def setup_messages(self):
        self.__messages__ = Messages(self)
        self.__messages__.grid(row=1, column=2, rowspan=2, columnspan=2, padx=5, pady=5, sticky='news')
    
    def get_screen(self):
        return self.__screen__
    
    def get_controls(self):
        return self.__controls__
    
    def get_connection(self):
        return self.__connection__
    
    def get_messages(self):
        return self.__messages__
    
    def setup_button_exit(self):
        __btn_exit__ = Button(self, text='EXIT')
        __btn_exit__.grid(row=3, column=2, rowspan=2, columnspan=2, padx=5, pady=5, sticky='news')
