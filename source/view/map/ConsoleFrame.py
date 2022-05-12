import tkinter


class ConsoleFrame(tkinter.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        self.size = 100
        self.button = None
        self.button_size = 50
        self.button_image = None
        self.field = None
        self.current_text = tkinter.StringVar()
        self.grid(row=1, column=0)

        self.__create_UI()

    def __create_UI(self):
        self.button_image = tkinter.PhotoImage(file='./assets/gitlab.png')
        self.button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                     image=self.button_image,
                                     command=lambda: self.clear_console())

        self.current_text.set("No port")

        label = tkinter.Label(self, textvariable=self.current_text, background='white')
        label.grid(row=0, column=0)
        self.button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

    def clear_console(self):
        self.current_text.set("")
