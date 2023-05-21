import tkinter
from data_structure.stringstack import StringStack

class StackGUI:

    def __init__(self, value):

        self.main_window = tkinter.Tk()
        self.value = value
        self.label = tkinter.Label(self.main_window, text=self.value)
        self.label.pack()
        tkinter.mainloop()

class StackInitGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="Введите максимальное количество элементов стэка:")
        self.size_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.size_entry.pack(side="left")

        self.return_value_btn = tkinter.Button(self.bottom_frame,
                                               text="Создать",
                                               command=self.return_value)
        self.quit_btn = tkinter.Button(self.bottom_frame,
                                       text="Выход",
                                       command=self.main_window.destroy)

        self.return_value_btn.pack(side="left")
        self.quit_btn.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def return_value(self):
        value = int(self.size_entry.get())
        self.main_window.destroy()
        StackGUI(value)