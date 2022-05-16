import tkinter
from source.control.DebugController import DebugController
from source.view.debug.DebugMode import DebugMode
from source.view.Font import Font
from source.model.chunks.Color import Color


class DebugFrame(tkinter.Frame):
    def __init__(self, main_window, width_ratio=0.1, height_ratio=0.5):
        # super class constructor
        super().__init__(main_window, background=Color.BACKGROUND.value, highlightbackground="black",
                         highlightthickness=2)

        # get main frame attribute
        self.main_window = main_window

        # configure frame
        self.grid(row=2, column=1)
        self.configure(width=self.main_window.winfo_width() * width_ratio,
                       height=self.main_window.winfo_height() * height_ratio)
        self.grid_propagate(False)

        # get debug singleton
        self.debugController = DebugController()

        # create UI
        self.__create_UI()

    def __create_UI(self):
        self.update()
        size = self.winfo_width()
        label = tkinter.Label(self, text="Liste des modes de debug",
                              font=Font.SOUS_TITRE.value,
                              background=Color.BACKGROUND.value,
                              fg=Color.WHITE.value,
                              wraplengt=size)

        label.pack(anchor=tkinter.CENTER, pady=(0, 15))

        vals = [e.value for e in DebugMode]
        etiqs = ['Position robot', 'Données lidar', 'Commandes envoyées']
        self.varGr = tkinter.StringVar()

        for i in range(len(etiqs)):
            b = tkinter.Radiobutton(self,
                                    variable=self.varGr,
                                    text=etiqs[i],
                                    value=vals[i],
                                    command=self.__add_debug_mode,
                                    tristatevalue=0,
                                    activebackground=Color.BACKGROUND.value,
                                    activeforeground=Color.WHITE.value,
                                    background=Color.BACKGROUND.value,
                                    selectcolor=Color.BACKGROUND.value,
                                    fg=Color.WHITE.value)
            b.pack(anchor=tkinter.W)

    def __add_debug_mode(self):
        self.debugController.fix_debug_mode(self.varGr.get().__str__())
        print(self.varGr.get().__str__())
