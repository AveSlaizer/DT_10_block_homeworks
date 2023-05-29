import tkinter
from data_structure.priority_queue import PriorityQueue, Task



class MainWindow:
    MW_GEOMETRY = "500x500"
    def __init__(self):
        self.queue = PriorityQueue()

        self.main_window = tkinter.Tk()
        self.main_window.title("To - Do List")
        #self.main_window.geometry(self.MW_GEOMETRY)

        self.main_window.columnconfigure(index=0, weight=45)
        self.main_window.columnconfigure(index=1, weight=45)

        self.main_window.rowconfigure(index=0, )

        self.actual_task = tkinter.StringVar()
        self.actual_task.set(self.queue.peek()) # <<<<<<<<<<<<<

        self.task_label = tkinter.Label(self.main_window, textvariable=self.actual_task, font=("Arial", 16),
                                        width=40, height=10, borderwidth=3, relief="ridge")
        self.task_label.grid(row=0, columnspan=2, sticky="wens", pady=4, padx=4)

        self.change_btn = tkinter.Button(self.main_window, text="Изменить", font=("Arial", 16))
        self.change_btn.grid(row=1, column=0, sticky="we", pady=8, padx=4)

        self.do_it_btn = tkinter.Button(self.main_window, text="Выполнить", font=("Arial", 16))
        self.do_it_btn.grid(row=1, column=1, sticky="we", pady=8, padx=4)

        self.add_btn = tkinter.Button(self.main_window, text="Добавить",font=("Arial", 16), width=22)
        self.add_btn.grid(row=2, columnspan=2, pady=4, padx=4)

        self.empty_label = tkinter.Label(self.main_window, height=10)
        self.empty_label.grid(row=4, columnspan=2)

        self.quit_btn = tkinter.Button(self.main_window, text="Выход", font=("Arial", 16), width=22)
        self.quit_btn.grid(row=4, columnspan=2)

        tkinter.mainloop()