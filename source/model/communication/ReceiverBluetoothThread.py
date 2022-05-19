import threading


class ReceiverBluetoothThread(threading.Thread):
    def __init__(self, bluetooth_manager, object_receiver):
        super().__init__()
        self.bluetooth_manager = bluetooth_manager
        self.object_receiver = object_receiver
        self.data = ""

    def run(self):
        while True:
            tmp = str(self.bluetooth_manager.socket.recv(self.bluetooth_manager.port), "UTF-8")
            self.data += tmp
            if tmp != '\n':
                # self.object_receiver.update(self.data)
                print(tmp)
                self.data = ""
