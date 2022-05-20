from source.view.MainWindow import MainWindow
from source.view.debug.DebugFrame import DebugFrame
from source.view.map.MapFrame import MapFrame
from source.view.map.MapViewerFrame import MapViewerFrame
from source.view.console.ConsoleFrame import ConsoleFrame
from source.view.command.CommandFrame import CommandFrame


def main():
    # main window
    main_window = MainWindow()

    # map frame
    map_frame = MapFrame(main_window)
    map_frame.map_frame_thread.start()

    # map viewer frame
    MapViewerFrame(main_window, map_frame)

    # command frame
    CommandFrame(main_window, map_frame)

    # debug frame
    DebugFrame(main_window)

    # console frame
    ConsoleFrame(main_window)

    # main loop
    main_window.mainloop()


if __name__ == '__main__':
    main()
