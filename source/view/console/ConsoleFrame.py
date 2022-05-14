import tkinter
from source.control.DebugController import DebugController


class ConsoleFrame(tkinter.Frame):
    def __init__(self, main_window, width_ratio=0.755, height_ratio=0.2):
        # super class constructor
        super().__init__(main_window, background='white', highlightbackground="black", highlightthickness=2)

        # get main frame attribute
        self.main_window = main_window

        # configure frame
        self.grid(row=2, column=0, padx=(10, 10), pady=(0, 10))
        self.configure(width=width_ratio * main_window.winfo_width(), height=height_ratio * main_window.winfo_height())
        self.grid_propagate(False)

        # attributs
        self.button = None
        self.button_size = 25
        self.button_image = None
        self.field = None

        # singleton class to get information to display
        self.debugController = DebugController()

        # init the UI to the window
        self.__create_UI()

    def __create_UI(self):
        # add the black console label
        label = tkinter.Label(self, textvariable=self.debugController.all_text, background='black', fg='white')
        label.grid(row=0, column=0)

        # add clear console button
        self.button_image = tkinter.PhotoImage(file='./assets/x-circle.png')
        self.button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                     image=self.button_image,
                                     command=lambda: self.__clear_console())
        self.button.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))

    def __clear_console(self):
        self.debugController.clear_text()
