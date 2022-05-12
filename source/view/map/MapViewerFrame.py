import tkinter
from source.view.serial_port.SerialPortWindow import SerialPortWindow

"""
Classe MapViewerFrame qui va gérer toute la partie gestion de la map (Humain-map)
"""


class MapViewerFrame(tkinter.Frame):
    def __init__(self, main_window, map_frame, width_ratio=0.1, height_ratio=0.45, button_size=50):
        super().__init__(main_window, background='white', highlightbackground="black", highlightthickness=2)

        self.main_window = main_window
        self.map_frame = map_frame
        self.button_size = button_size
        self.grid(row=0, column=1)

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

        self.serial_port_button = None

        self.create_view()

    def create_view(self):
        self.step_scale = tkinter.Scale(self, orient='horizontal', from_=1, to=5, resolution=1, tickinterval=2,
                                        background="white", bd=0, relief="flat")

        self.serial_port_button = tkinter.Button(self, width=self.button_size, height=self.button_size,
                                                image=self.left_arrow_image,
                                                command=lambda: self.serial_port_action())

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
                                          bg='#FDD698')
        self.robot_position_button = tkinter.Button(self, width=self.button_size, height=self.button_size, bg='#FDD698',
                                                    image=self.robot_position_image)

        self.left_arrow_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
        self.right_arrow_button.grid(row=1, column=2, padx=(10, 10), pady=(10, 10))
        self.up_arrow_button.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))
        self.down_arrow_button.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))
        self.home_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10))
        self.robot_position_button.grid(row=0, column=2, padx=(10, 10), pady=(10, 10))

        self.step_scale.grid(row=3, column=0, columnspan=3, sticky='ew', padx=(5, 10), pady=(5, 10))

        self.serial_port_button.grid(row=4, column=0, columnspan=3, sticky='ew', padx=(5, 10), pady=(5, 10))

    def update_map_frame(self, x_direction, y_direction):
        self.map_frame.update_camera_center(self.map_frame.camera_center_x + x_direction * self.step_scale.get(),
                                            self.map_frame.camera_center_y + y_direction * self.step_scale.get())

    def serial_port_action(self):
        port_window = SerialPortWindow()
        port_window.mainloop()
