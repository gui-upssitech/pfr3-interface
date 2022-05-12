from source.view.MainWindow import MainWindow
from source.model.communication.SerialManager import SerialManager
from source.view.map.MapFrame import MapFrame
from source.view.map.MapViewerFrame import MapViewerFrame
from source.view.map.ConsoleFrame import ConsoleFrame


def main():
    # main window
    main_window = MainWindow()

    # map frame
    map_frame = MapFrame(main_window)
    map_frame.map_frame_thread.start()

    # map viewer frame
    MapViewerFrame(main_window, map_frame)
    ConsoleFrame(main_window)

    # command frame

    # serial
    serial_communication = SerialManager('COM5')
    serial_communication.start()

    main_window.mainloop()


if __name__ == '__main__':
    main()
