import tkinter
import sys
import glob
import serial

from source.view.Font import Font


class SerialPortWindow(tkinter.Tk):
    def __init__(self, width_window=250, height_window=300):
        super().__init__()
        self.listbox = None
        self.label_text = tkinter.StringVar()
        self.selected_port = None
        self.resizable(width=False, height=False)
        self.title('Serial Port')
        self.configure(background='white')
        self.grid_rowconfigure(0, weight=3)
        self.grid_columnconfigure(0, weight=1)
        self.geometry(str(width_window) + 'x' + str(height_window))

        self.create_list_serial()
        self.create_label()

    def create_label(self):
        label = tkinter.Label(self, text="Liste des Serial Ports", font=Font.TITRE.value,background='white')
        label.grid(row=0, column=0)

        self.label_text.set("No port")
        selected_label = tkinter.Label(self, textvariable=self.label_text, font=Font.SOUS_TITRE.value, background='white')
        selected_label.grid(row=1, column=0)

    def create_list_serial(self):
        # get list of serial port available from pc
        list_serial = self.__get_serial_ports()

        # Trash example test
        langs = ('COM7', 'COM9', 'COM10')

        langs_var = tkinter.StringVar(value=list_serial)

        self.listbox = tkinter.Listbox(
            self,
            listvariable=langs_var,
            height=6)

        self.listbox.grid(
            column=0,
            row=2,
            pady=(0,10)
        )

        self.listbox.bind('<<ListboxSelect>>', self.items_selected)

    # handle event
    def items_selected(self, event):
        """ handle item selected event
        """
        # get selected indices
        selected_indices = self.listbox.curselection()

        # get selected items
        selected_langs = ",".join([self.listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'

        self.label_text.set("Port actuel : " + selected_langs)
        print(msg)

    # source : https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
    def __get_serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result


if __name__ == '__main__':
    main_window = SerialPortWindow()
    main_window.mainloop()
