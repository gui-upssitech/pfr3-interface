import tkinter
from source.view.debug.DebugMode import DebugMode


def singleton_dec(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton_dec
class DebugController:
    def __init__(self):
        self.line_counter = 0
        self.all_text = tkinter.StringVar()
        self.all_text.set("> ")

        # dict 0 => not activate 1 => activate
        self.dictionnary = {}

        # init
        tab_mode = [e.value for e in DebugMode]
        for i in range(len(tab_mode)):
            self.dictionnary[tab_mode[i]] = 0

    def get_mode(self, mode):
        return self.dictionnary[mode]

    # WARNING = mode need to be a string
    def fix_debug_mode(self, mode):
        for key in self.dictionnary:
            # set the new mode to 1
            if mode == key:
                self.dictionnary[key] = 1
            # reset value from the older mode
            elif mode != key and int(self.dictionnary[key]) == 1:
                self.dictionnary[key] = 0

    def add_new_line(self, text):
        if self.line_counter < 2:
            self.all_text.set(self.all_text.get() + "\n" + text)
            self.line_counter += 1

    def clear_text(self):
        self.all_text.set("> ")
        self.line_counter = 0

    def __str__(self):
        string = ""
        for key in self.dictionnary:
            string += str(key) + '->' + str(self.dictionnary[key]) + "\n"

        return string

# if __name__ == '__main__':
#     debug = DebugController()
#     print(debug)
#     debug.fix_debug_mode(DebugMode.LIDAR.value)
#     print(str(debug))
#     debug.fix_debug_mode(DebugMode.LIDAR.value)
#     print(str(debug))
