import tkinter
from source.model.chunks.Color import Color

"""
Classe MapViewerFrame qui va gérer toute la partie gestion de la map (Humain-map)
"""


class MapViewerFrame(tkinter.Frame):
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
        self.grid(row=0, column=1)
        self.configure(width=self.main_window.winfo_width() * width_ratio,
                       height=self.main_window.winfo_height() * height_ratio)
        self.pack_propagate(False)

        # set widgets
        self.left_arrow_button = None
        self.left_arrow_image = tkinter.PhotoImage(file='./assets/arrow-left.png')
        self.right_arrow_button = None
        self.right_arrow_image = tkinter.PhotoImage(file='./assets/arrow-right.png')
        self.up_arrow_button = None
        self.up_arrow_image = tkinter.PhotoImage(file='./assets/arrow-up.png')
        self.down_arrow_button = None
        self.down_arrow_image = tkinter.PhotoImage(file='./assets/arrow-down.png')

        self.home_button = None
        self.home_image = tkinter.PhotoImage(file='./assets/home.png')
        self.robot_position_button = None
        self.robot_position_image = tkinter.PhotoImage(file='./assets/gitlab.png')

        self.step_scale = None

        # create the view
        self.create_view()

    def create_view(self):
        self.step_scale = tkinter.Scale(self, orient='horizontal', from_=1, to=5, resolution=1, tickinterval=2,
                                        background=Color.BACKGROUND.value,
                                        fg=Color.WHITE.value,
                                        bd=0, relief="flat")

        # create all buttons
        self.left_arrow_button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                                image=self.left_arrow_image,
                                                command=lambda: self.update_map_frame(-1, 0))
        self.right_arrow_button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                                 image=self.right_arrow_image,
                                                 command=lambda: self.update_map_frame(1, 0))
        self.up_arrow_button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                              image=self.up_arrow_image, command=lambda: self.update_map_frame(0, 1))
        self.down_arrow_button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                                image=self.down_arrow_image,
                                                command=lambda: self.update_map_frame(0, -1))

        self.home_button = tkinter.Button(self, width=self.button_size, height=self.button_size, image=self.home_image,
                                          bg=Color.ORANGE.value)
        self.robot_position_button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                                    bg=Color.ORANGE.value,
                                                    image=self.robot_position_image)

        # grid all the buttons
        self.left_arrow_button.grid(row=1, column=0, padx=(self.paddingx, self.paddingx),
                                    pady=(self.paddingy, self.paddingy))
        self.right_arrow_button.grid(row=1, column=2, padx=(self.paddingx, self.paddingx),
                                     pady=(self.paddingy, self.paddingy))
        self.up_arrow_button.grid(row=0, column=1, padx=(self.paddingx, self.paddingx),
                                  pady=(self.paddingy, self.paddingy))
        self.down_arrow_button.grid(row=1, column=1, padx=(self.paddingx, self.paddingx),
                                    pady=(self.paddingy, self.paddingy))
        self.home_button.grid(row=0, column=0, padx=(self.paddingx, self.paddingx), pady=(self.paddingy, self.paddingy))
        self.robot_position_button.grid(row=0, column=2, padx=(self.paddingx, self.paddingx),
                                        pady=(self.paddingy, self.paddingy))
        self.step_scale.grid(row=3, column=0, columnspan=3, sticky='ew', padx=(self.paddingx / 2, self.paddingx),
                             pady=(self.paddingy / 2, self.paddingy))

    def update_map_frame(self, x_direction, y_direction):
        self.map_frame.update_camera_center(self.map_frame.camera_center_x + x_direction * self.step_scale.get(),
                                            self.map_frame.camera_center_y + y_direction * self.step_scale.get())
