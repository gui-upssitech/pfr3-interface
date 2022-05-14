import threading
import re
from source.model.chunks.ChunkManager import ChunkManager
from source.control.DebugController import DebugController
from source.view.debug.DebugMode import DebugMode

"""
Classe SerialThread qui hérite de Thread qui va lire en continu les données envoyés par l'arduino
En même de lire les données, on va ajouter ces données directement dans le chunkManager
"""


class SerialThread(threading.Thread):
    def __init__(self, serial_manager):
        super().__init__()
        self.serial_manager = serial_manager
        self.chunk_manager = ChunkManager(100)
        self.debug_controller = DebugController()
        self.regex = '^-?[\d]+,-?[\d]+$'

    def run(self):
        while True:
            line = (self.serial_manager.communication.readline()).decode("utf-8").rstrip()

            if re.match(self.regex, line):
                coords = line.split(",")
                if self.debug_controller.get_mode(DebugMode.LIDAR.value) == 1:
                    self.debug_controller.add_new_line(line)

                self.chunk_manager.increment_case(int(coords[0]), int(coords[1]))
