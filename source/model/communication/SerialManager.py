import serial
from serial import SerialException
from source.model.communication.SerialThread import SerialThread

"""
Classe SerialManager qui gère la lecture des données du port. 
Ces données sont envoyées directement par l'arduino par bluetooth
"""
class SerialManager():
    def __init__(self, port, baud_rate=250000):
        # serial communication initalization
        try:
            self.port = port
            self.communication = serial.Serial(port=port, baudrate=baud_rate,
                                               bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE)
        except SerialException:
            raise

        self.serial_thread = SerialThread(self)

    def start(self):
        self.serial_thread.start()
