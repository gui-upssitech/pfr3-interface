import tkinter
from source.model.chunks.Color import Color


class MainWindow(tkinter.Tk):
    def __init__(self, width_window=1200, height_window=700):
        super().__init__()
        self.resizable(width=False, height=False)
        self.title('BT-YT')
        self.configure(background=Color.BACKGROUND.value)
        self.geometry(str(width_window) + 'x' + str(height_window))
        self.update()
