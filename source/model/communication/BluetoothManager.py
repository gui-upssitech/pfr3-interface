import bluetooth

from source.model.communication.ReceiverBluetoothThread import ReceiverBluetoothThread
from source.model.communication.SenderBluetoothThread import SenderBluetoothThread

"""
Classe BluetoothManager qui gère la connexion à un apparail bluetooth afin de lire ces données
"""


class BluetoothManager:
    def __init__(self, device_name, port, object_receiver):
        self.port = port
        self.object_receiver = object_receiver # object linked to thread ex : recevied data from lidar => ChunkManager
        self.device_name = device_name
        self.device_mac = None
        self.socket = None
        self.sender = None
        self.receiver = None

    def init(self):
        # step 1 : find the device with his bluetooth name
        self.__find_device()
        if self.device_mac is None:
            print("Error connecting to " + self.device_name + ".")
        else:
            print("Connected to " + self.device_name + ".")
            # step 2 : create the socket
            self.__create_socket()

            # step 3 : create threads
            self.sender = SenderBluetoothThread(self, self.object_receiver)
            self.receiver = ReceiverBluetoothThread(self, self.object_receiver)

    def start(self, receiver=False, sender=False):
        if self.sender is not None and sender is True:
            self.sender.start()

        if self.receiver is not None and receiver is True:
            self.receiver.start()

    def end(self):
        if self.socket is not None:
            self.socket.close()
            print("Socket closed... - " + self.device_name + ".")
        else:
            print("Impossible to close " + self.device_name + ".")

    def send(self, data):
        if self.socket is not None:
            self.socket.send(data)

    def __find_device(self):
        devices_list = bluetooth.discover_devices()

        for bdaddr in devices_list:
            print(bluetooth.lookup_name(bdaddr))
            if self.device_name == bluetooth.lookup_name(bdaddr):
                self.device_mac = bdaddr
                break

    def __create_socket(self):
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.socket.connect((self.device_mac, self.port))


if __name__ == '__main__':
    bt = BluetoothManager("Xbox Wireless Controller", 1, None)
    bt.init()
    bt.start(receiver=True)
