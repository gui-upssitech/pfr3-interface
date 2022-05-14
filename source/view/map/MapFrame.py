import math
import tkinter
from source.model.chunks.ChunkManager import ChunkManager
from source.model.chunks.filter.hough_filter import *
from source.view.map.ChunkCanva import ChunkCanva
from source.view.map.MapFrameThread import MapFrameThread


class MapFrame(tkinter.Frame):
    def __init__(self, main_window, width_ratio=0.8, height_ratio=0.85):
        # super class constructor
        super().__init__(main_window,
                         highlightbackground="black",
                         highlightthickness=2)

        # get main frame attribute
        self.main_window = main_window

        # canvas parameters
        self.canva_size = 100
        self.map_canvas = []

        # get max x and max y to display on the frame
        self.max_canvas_x, self.max_canvas_y = int(
            self.main_window.winfo_width() * width_ratio) // self.canva_size, \
                                               int(self.main_window.winfo_height() * height_ratio) // self.canva_size

        # configure frame
        self.grid(row=0, column=0, rowspan=2, sticky='ns', padx=(10, 10), pady=(10, 10))
        self.configure(width=self.max_canvas_x * self.canva_size, height=self.max_canvas_y * self.canva_size)
        self.grid_propagate(False)

        # coordinates of the center of the frame
        self.camera_center_x, self.camera_center_y = 0, 0

        # thread instance
        self.map_frame_thread = MapFrameThread(self)

    def update_camera_center(self, camera_center_x, camera_center_y):
        self.camera_center_x, self.camera_center_y = camera_center_x, camera_center_y

    def add_chunk_canva(self, filtered_chunk):
        # find if this canvas has to be updated or created
        for i in range(len(self.map_canvas)):
            if self.map_canvas[i].filtered_chunk.coords == filtered_chunk.coords:
                self.map_canvas[i].update_chunk_canva(filtered_chunk)
                return self.map_canvas[i]

        # if it doesnt exist, we create it
        self.map_canvas.append(ChunkCanva(filtered_chunk, self, self.canva_size, self.canva_size))
        return self.map_canvas[len(self.map_canvas) - 1]

    def update_map_frame(self):
        chunk_manager = ChunkManager(100)

        for i in range(len(chunk_manager.chunks_list)):
            if chunk_manager.chunks_list[i].coords[0] >= (self.camera_center_x - self.max_canvas_x // 2):
                if chunk_manager.chunks_list[i].coords[0] < (self.camera_center_x + math.ceil(self.max_canvas_x // 2)):
                    if chunk_manager.chunks_list[i].coords[1] >= (self.camera_center_y - self.max_canvas_y // 2):
                        if chunk_manager.chunks_list[i].coords[1] < (
                                self.camera_center_y + math.ceil(self.max_canvas_y // 2)):
                            # filtered_chunk = FilteredChunk(chunk_manager.chunks_list[i]).filter_simple()
                            filtered_chunk = apply_hough_filter(chunk_manager.chunks_list[i])
                            self.add_chunk_canva(filtered_chunk)

        # create / update the frame
        if len(self.map_canvas) > 0:
            for i in range(self.max_canvas_x):
                for j in range(self.max_canvas_y):
                    for k in range(len(self.map_canvas)):
                        if self.map_canvas[k].filtered_chunk.coords == (
                                self.camera_center_x + i - self.max_canvas_x // 2,
                                self.camera_center_y + j - self.max_canvas_y // 2):
                            self.map_canvas[k].canva.grid(row=self.max_canvas_y - j, column=i)
