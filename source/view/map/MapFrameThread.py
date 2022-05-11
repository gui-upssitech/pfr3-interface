import threading
import time


class MapFrameThread(threading.Thread):
    def __init__(self, map_frame, sleep_time=0.05):
        super().__init__()
        self.map_frame = map_frame
        self.sleep_time = sleep_time

    def run(self):
        while True:
            time.sleep(self.sleep_time)
            self.map_frame.update_map_frame()
