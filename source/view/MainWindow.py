import tkinter


class MainWindow(tkinter.Tk):
    def __init__(self, width_window=1200, height_window=700):
        super().__init__()
        self.resizable(width=False, height=False)
        self.title('BT-YT')
        self.configure(background='white')
        self.geometry(str(width_window) + 'x' + str(height_window))
