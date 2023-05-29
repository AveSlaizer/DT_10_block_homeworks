import tkinter
from data_structure.priority_queue import PriorityQueue, Task



class MainWindow:
    def __init__(self):
        self.queue = PriorityQueue()

        self.main_window = tkinter.Tk()
        self.main_window.title("To - Do List")

        tkinter.mainloop()