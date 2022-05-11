import tkinter
from source.model.chunks.ChunkManager import ChunkManager
from source.model.chunks.FilteredChunk import FilteredChunk
from source.view.map.ChunkCanva import ChunkCanva
from source.view.map.MapFrameThread import MapFrameThread

"""
Classe MapFrame qui gèrte l'interface de la map au centre de l'application
"""


class MapFrame(tkinter.Frame):
    def __init__(self, main_window, width_ratio=0.9, height_ratio=0.9):
        super().__init__(main_window, highlightbackground="black",  highlightthickness=2)
        self.main_window = main_window
        self.main_window.update()
        self.grid(row=0, column=0, sticky='ns')
        self.map_canvas = []
        self.min_x, self.max_x = 0, 0
        self.min_y, self.max_y = 0, 0
        self.width_canva, self.height_canva = 100, 100
        self.max_canvas_x, self.max_canvas_y = int(
            self.main_window.winfo_width() * width_ratio) // self.height_canva - 1, \
                                               int(self.main_window.winfo_height() * height_ratio) // self.height_canva - 1

        self.camera_center_x, self.camera_center_y = 0, 0

        self.map_frame_thread = MapFrameThread(self)

    def update_camera_center(self, camera_center_x, camera_center_y):
        self.camera_center_x, self.camera_center_y = camera_center_x, camera_center_y
        print("Updated: ", self.camera_center_x, self.camera_center_y)

    def add_chunk_canva(self, filtered_chunk):
        # find max scale for display
        if filtered_chunk.coords[0] < self.min_x:
            self.min_x = filtered_chunk.coords[0]

        if filtered_chunk.coords[0] > self.max_x:
            self.max_x = filtered_chunk.coords[0]

        if filtered_chunk.coords[1] < self.min_y:
            self.min_y = filtered_chunk.coords[1]

        if filtered_chunk.coords[1] > self.max_y:
            self.max_y = filtered_chunk.coords[1]

        # find if this canvas has to be updated or created
        for i in range(len(self.map_canvas)):
            if self.map_canvas[i].filtered_chunk.coords == filtered_chunk.coords:
                self.map_canvas[i].update_chunk_canva(filtered_chunk)
                return

        # if it doesnt exist, we create it
        self.map_canvas.append(ChunkCanva(filtered_chunk, self, self.width_canva, self.height_canva))

    def update_map_frame(self):
        chunk_manager = ChunkManager(100)

        for i in range(len(chunk_manager.chunks_list)):
            if chunk_manager.chunks_list[i].coords[0] >= (self.camera_center_x - self.max_canvas_x):
                if chunk_manager.chunks_list[i].coords[0] <= (self.camera_center_x + self.max_canvas_x):
                    if chunk_manager.chunks_list[i].coords[1] >= (self.camera_center_y - self.max_canvas_y):
                        if chunk_manager.chunks_list[i].coords[1] <= (self.camera_center_y + self.max_canvas_y):
                            filtered_chunk = FilteredChunk(chunk_manager.chunks_list[i]).filter_chunk_average()
                            self.add_chunk_canva(filtered_chunk)
                            if chunk_manager.chunks_list[i].coords[0] == -1 and chunk_manager.chunks_list[i].coords[1] == -1:
                                print(chunk_manager.chunks_list[i])

        # create the frame
        if len(self.map_canvas) > 0:
            for i in range(self.max_canvas_x):
                for j in range(self.max_canvas_y):
                    found = False
                    for k in range(len(self.map_canvas)):
                        if self.map_canvas[k].filtered_chunk.coords == (
                                self.camera_center_x + i - self.max_canvas_x // 2,
                                self.camera_center_y + j - self.max_canvas_y // 2):
                            self.map_canvas[k].canva.grid(row=j, column=i)
                            found = True
                            break

                    if not found:
                        white_canva = self.grid_slaves(row=j, column=i)
                        if not white_canva:
                            tkinter.Canvas(self, width=self.map_canvas[0].width_canva,
                                           height=self.map_canvas[0].height_canva,
                                           background='white', bd=0).grid(row=j, column=i)
