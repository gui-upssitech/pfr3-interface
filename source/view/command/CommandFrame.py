import tkinter


class CommandFrame(tkinter.Frame):
    def __init__(self, main_window, width_ratio=0.9, height_ratio=1):
        super().__init__(highlightbackground="black",  highlightthickness=2)
        self.main_window = main_window
        self.main_window.update()
        self.grid(row=0, column=1)
        