from source.model.chunks.Chunk import Chunk

"""
Classe ChunkManager qui va stocker et gérer tous les chunks présent sur la map.
IMPORTANT : Cette classe est un singleton !
"""


def singleton_dec(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton_dec
class ChunkManager:
    def __init__(self, size):
        self.size = size
        self.chunks_list = []

    def increment_case(self, x, y):
        (xChunk, yChunk) = x // self.size, y // self.size
        self.get_chunk(xChunk, yChunk).increment_case(x - self.size * xChunk, y - self.size * yChunk)

    def create_empty_chunk(self, xChunk, yChunk):
        chunk = Chunk((xChunk, yChunk), self.size)
        self.chunks_list.append(chunk)

    def get_chunk(self, xChunk, yChunk):
        for chunk in self.chunks_list:
            if (xChunk, yChunk) == chunk.coords:
                return chunk
        chunk = Chunk((xChunk, yChunk), self.size)
        self.chunks_list.append(chunk)
        return chunk
