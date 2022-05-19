import threading
import time


class SenderBluetoothThread(threading.Thread):
    def __init__(self, bluetooth_manager, object_receiver, sleep_time=0.05):
        super().__init__()
        self.bluetooth_manager = bluetooth_manager
        self.object_receiver = object_receiver
        self.sleep_time = sleep_time

    def run(self):
        while True:
            if self.object_receiver.tmp_data != "":
                self.bluetooth_manager.socket.send(self.object_receiver.tmp_data)
                self.object_receiver.tmp_data = ""
                time.sleep(self.sleep_time)
