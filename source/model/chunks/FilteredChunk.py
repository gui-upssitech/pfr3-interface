from source.model.chunks.Chunk import Chunk
from source.model.chunks.Pattern import Pattern

"""
Classe FilteredChunk qui est un chunk mais avec un certain filtre appliqué
"""
class FilteredChunk:
    def __init__(self, chunk):
        self.chunk = chunk

    def erode(self, pattern):
        filtered_chunk = Chunk(self.chunk.coords, self.chunk.size)

        if pattern == Pattern.SQUARE_3:
            for i in range(self.chunk.size):
                for j in range(self.chunk.size):
                    min_value = 1
                    for m in range(-1, 2):
                        for n in range(-1, 2):
                            x = i + m
                            y = j + n

                            if x < 0 or x >= self.chunk.size:
                                min_value = 0

                            elif y < 0 or y >= self.chunk.size:
                                min_value = 0

                            elif self.chunk.chunk[x][y] < min_value:
                                min_value = self.chunk.chunk[i + m][j + n]
                    filtered_chunk.chunk[i][j] = min_value
        return filtered_chunk

    def dilate(self, pattern):
        filtered_chunk = Chunk(self.chunk.coords, self.chunk.size)

        if pattern == Pattern.SQUARE_3:
            for i in range(self.chunk.size):
                for j in range(self.chunk.size):
                    max_value = 0
                    for m in range(-1, 2):
                        for n in range(-1, 2):
                            x = i + m
                            y = j + n

                            if x < 0 or x >= self.chunk.size:
                                max_value = 0

                            elif y < 0 or y >= self.chunk.size:
                                max_value = 0

                            elif self.chunk.chunk[x][y] > max_value:
                                max_value = self.chunk.chunk[i + m][j + n]
                    filtered_chunk.chunk[i][j] = max_value
        return filtered_chunk

    def filter_chunk_no_zero_average(self):
        filtered_chunk = Chunk(self.chunk.coords, self.chunk.size)
        total = 0
        size = 0

        for i in range(self.chunk.size):
            for j in range(self.chunk.size):
                if self.chunk.chunk[i][j] > 0:
                    size += 1
                    total += self.chunk.chunk[i][j]

        k_average = total // size

        for i in range(self.chunk.size):
            for j in range(self.chunk.size):
                if self.chunk.chunk[i][j] >= k_average:
                    filtered_chunk.increment_case(i, j)

        return filtered_chunk

    def filter_chunk_average(self):
        average = self.chunk.get_average()
        filtered_chunk = Chunk(self.chunk.coords, self.chunk.size)
        for i in range(self.chunk.size):
            for j in range(self.chunk.size):
                if self.chunk.chunk[i][j] >= average:
                    filtered_chunk.increment_case(i, j)
        return filtered_chunk
