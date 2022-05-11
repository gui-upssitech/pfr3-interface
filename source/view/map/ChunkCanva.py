import tkinter


class ChunkCanva:
    def __init__(self, filtered_chunk, map_frame, width_canva=200, height_canva=200, cm_pixel_size=2,
                 show_coords=True):
        # TODO : check attributes' values
        self.width_canva = width_canva
        self.height_canva = height_canva
        self.cm_pixel_size = cm_pixel_size
        self.filtered_chunk = filtered_chunk
        self.old_filtered_chunk = filtered_chunk
        self.map_frame = map_frame
        self.show_coords = show_coords
        self.canva = tkinter.Canvas(self.map_frame, width=self.width_canva, height=self.height_canva,
                                    background='white', bd=0)

    def update_chunk_canva(self, filtered_chunk):
        self.__update_chunk(filtered_chunk)
        self.__update_view()

    def __update_chunk(self, filtered_chunk):
        self.old_filtered_chunk = self.filtered_chunk
        self.filtered_chunk = filtered_chunk

    def __update_view(self):
        if self.show_coords:
            self.canva.create_text(self.width_canva / 2, self.height_canva / 2,
                                   text=(str(self.filtered_chunk.coords[0]) + "," + str(self.filtered_chunk.coords[1])))

        for i in range(self.filtered_chunk.size):
            for j in range(self.filtered_chunk.size):
                if self.filtered_chunk.chunk[i][j] != self.old_filtered_chunk.chunk[i][j]:
                    if self.filtered_chunk.chunk[i][j] == 0:
                        self.canva.create_rectangle(self.cm_pixel_size * i, self.cm_pixel_size * j,
                                                    self.cm_pixel_size * (i + 1), self.cm_pixel_size * (j + 1),
                                                    fill='white', outline="")
                    elif self.filtered_chunk.chunk[i][j] == 1:
                        self.canva.create_rectangle(self.cm_pixel_size * i, self.cm_pixel_size * j,
                                                    self.cm_pixel_size * (i + 1), self.cm_pixel_size * (j + 1),
                                                    fill='red', outline="")
