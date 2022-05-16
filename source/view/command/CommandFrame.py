import tkinter
from source.model.chunks.Color import Color

"""
Classe MapViewerFrame qui va gérer toute la partie gestion de la map (Humain-map)
"""


class CommandFrame(tkinter.Frame):
    def __init__(self, main_window, map_frame, width_ratio=0.1, height_ratio=0.5, button_size=40):
        # super class constructor
        super().__init__(main_window, background='#303041', highlightbackground="black", highlightthickness=2)

        # get main frame attribute
        self.main_window = main_window
        self.map_frame = map_frame
        self.button_size = button_size
        self.paddingx = 5
        self.paddingy = 5

        # configure frame
        self.grid(row=1, column=1)
        self.configure(width=self.main_window.winfo_width() * width_ratio,
                       height=self.main_window.winfo_height() * height_ratio)
        self.pack_propagate(False)

        # set widgets
        self.mode_button = None
        self.button_image = tkinter.PhotoImage(file='./assets/user.png')
        self.is_manual = False

        self.label = None
        self.label_text = tkinter.StringVar()
        self.label_text.set("Mode Automatique")

        # create the view
        self.create_view()

    def create_view(self):
        # create all buttons
        self.mode_button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                          image=self.button_image, bg=Color.ORANGE.value,
                                          command=self.__set_robot_mode)

        self.label = tkinter.Label(self, textvariable=self.label_text, bg=Color.BACKGROUND.value,
                                   foreground=Color.WHITE.value)

        # grid all the buttons
        self.mode_button.grid(row=1, column=0, padx=(self.paddingx, self.paddingx),
                              pady=(self.paddingy, self.paddingy))
        self.label.grid(row=1, column=1, padx=(self.paddingx, self.paddingx),
                        pady=(self.paddingy, self.paddingy))

    def __set_robot_mode(self):
        if self.is_manual:
            self.is_manual = False
            self.button_image = tkinter.PhotoImage(file='./assets/user.png')
            self.mode_button.configure(image=self.button_image)
            self.label_text.set("Mode Automatique")

        else:
            self.is_manual = True
            self.button_image = tkinter.PhotoImage(file='./assets/user-x.png')
            self.mode_button.configure(image=self.button_image)
            self.label_text.set("Mode Manuel          ")
