import threading
from source.model.chunks.ChunkManager import ChunkManager

"""
Classe SerialThread qui hérite de Thread qui va lire en continu les données envoyés par l'arduino
En même de lire les données, on va ajouter ces données directement dans le chunkManager
"""


class SerialThread(threading.Thread):
    def __init__(self, serial_manager):
        super().__init__()
        self.serial_manager = serial_manager
        self.chunk_manager = ChunkManager(100)

    def run(self):
        while True:

            try:
                line = (self.serial_manager.communication.readline()).decode("utf-8").rstrip()
            except:
                print("Error detected : " + str(line))
            coords = line.split(",")
            if len(coords) == 2 and coords[0] != '' and coords[1] != '':
                self.chunk_manager.increment_case(int(coords[0]), int(coords[1]))
