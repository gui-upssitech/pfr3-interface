import tkinter


class ChunkCanva:
    def __init__(self, filtered_chunk, map_frame, chunk_size=100, canva_size=200, show_coords=True):
        # TODO : check attributes
        self.chunk_size = chunk_size
        self.canva_size = canva_size
        self.pixel_resolution = canva_size // chunk_size
        self.filtered_chunk = filtered_chunk
        self.old_filtered_chunk = filtered_chunk
        self.map_frame = map_frame
        self.show_coords = show_coords
        self.canva = tkinter.Canvas(self.map_frame, width=self.canva_size, height=self.canva_size,
                                    background='white', borderwidth=0, highlightthickness=0)

    def update_chunk_canva(self, filtered_chunk):
        self.__update_chunk(filtered_chunk)
        self.__update_view()

    def __update_chunk(self, filtered_chunk):
        self.old_filtered_chunk = self.filtered_chunk
        self.filtered_chunk = filtered_chunk

    def __update_view(self):
        if self.show_coords:
            self.canva.create_text(self.canva_size / 2, self.canva_size / 2,
                                   text=(str(self.filtered_chunk.coords[0]) + "," + str(self.filtered_chunk.coords[1])))

        for i in range(self.filtered_chunk.size):
            for j in range(self.filtered_chunk.size):
                if self.filtered_chunk.chunk[i][j] != self.old_filtered_chunk.chunk[i][j]:
                    if self.filtered_chunk.chunk[i][j] == 0:
                        self.canva.create_rectangle((self.pixel_resolution * i,
                                                    self.pixel_resolution * (self.chunk_size - j)) * 2,
                                                    fill='white', outline="")
                    elif self.filtered_chunk.chunk[i][j] == 1:
                        self.canva.create_rectangle((self.pixel_resolution * i,
                                                    self.pixel_resolution * (self.chunk_size - j)) * 2,
                                                    fill='red', outline="")
