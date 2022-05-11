import time

from source.view.MainWindow import MainWindow
from source.model.communication.SerialManager import SerialManager
from source.view.map.MapFrame import MapFrame
from source.view.map.MapViewerFrame import MapViewerFrame


def main():
    # main window
    main_window = MainWindow()

    # map frame
    map_frame = MapFrame(main_window)
    map_frame.map_frame_thread.start()

    # map viewer frame
    map_viewer_frame = MapViewerFrame(main_window, map_frame)

    # command frame

    # serial
    #serial_communication = SerialManager('COM7')
    #serial_communication.start()

    main_window.mainloop()


if __name__ == '__main__':
    main()
