import re

from math import floor
from source.model.chunks.Chunk import Chunk
from source.control.DebugController import DebugController
from source.view.debug.DebugMode import DebugMode


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
        self.regex = "^-?[\d]+,-?[\d]+,-?[\d]+,-?[\d]+$"

    def increment_case(self, x, y):
        (xChunk, yChunk) = floor(x / self.size), floor(y / self.size)
        self.get_chunk(xChunk, yChunk).increment_case(x % self.size, y % self.size)

    def get_chunk(self, xChunk, yChunk):
        for chunk in self.chunks_list:
            if (xChunk, yChunk) == chunk.coords:
                return chunk
        chunk = Chunk((xChunk, yChunk), self.size)
        self.chunks_list.append(chunk)
        return chunk

    def update(self, data):
        if re.match(self.regex, data):
            coords = data.split(",")
            if self.debug_controller.get_mode(DebugMode.LIDAR.value) == 1:
                self.debug_controller.add_new_line(data)

            self.chunk_manager.increment_case(int(coords[0]), int(coords[1]))

            # TODO get coords robot, do something with them
