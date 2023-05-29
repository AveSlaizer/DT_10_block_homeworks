import tkinter
from tkinter import messagebox
from data_structure.priority_queue import PriorityQueue, Task


class MainWindow:

    def __init__(self):
        self.queue = PriorityQueue()

        self.main_window = tkinter.Tk()
        self.main_window.title("To - Do List")

        self.main_window.columnconfigure(index=0, weight=45)
        self.main_window.columnconfigure(index=1, weight=45)

        self.main_window.rowconfigure(index=0, )

        self.actual_task = tkinter.StringVar()
        self.actual_task.set(self.queue.peek())

        self.task_label = tkinter.Label(self.main_window, textvariable=self.actual_task, font=("Arial", 16),
                                        width=40, height=10, borderwidth=3, relief="ridge")
        self.task_label.grid(row=0, columnspan=2, sticky="wens", pady=4, padx=4)

        self.change_btn = tkinter.Button(self.main_window, text="Изменить", font=("Arial", 16),
                                         command=self.__change_actual_task_priority, state="disabled")
        self.change_btn.grid(row=1, column=0, sticky="we", pady=8, padx=4)

        self.do_it_btn = tkinter.Button(self.main_window, text="Выполнить", font=("Arial", 16), state="disabled")
        self.do_it_btn.grid(row=1, column=1, sticky="we", pady=8, padx=4)

        self.add_btn = tkinter.Button(self.main_window, text="Добавить", font=("Arial", 16), width=22,
                                      command=self.__add_task_window)
        self.add_btn.grid(row=2, columnspan=2, pady=4, padx=4)

        self.empty_label = tkinter.Label(self.main_window, height=10)
        self.empty_label.grid(row=4, columnspan=2)

        self.quit_btn = tkinter.Button(self.main_window, text="Выход", font=("Arial", 16), width=22,
                                       command=self.main_window.destroy)
        self.quit_btn.grid(row=4, columnspan=2)

        tkinter.mainloop()

    def __change_actual_task_priority(self):
        self.main_window.state("icon")
        self.change_window = tkinter.Tk()
        self.change_window.title("Change priority")

        self.new_priority = tkinter.StringVar()

        self.priority_change_spinbox = tkinter.Spinbox(self.change_window, from_=1, to=10, font=("Arial", 16))
        #self.new_priority.set(self.priority_change_spinbox.get())
        self.priority_change_spinbox.grid(row=0, columnspan=2, pady=4, padx=4)

        self.ok_btn = tkinter.Button(self.change_window, text="OK", font=("Arial", 16), width=10)
        self.ok_btn.grid(row=1, column=0, pady=4, padx=4)

        self.cancel_change_btn = tkinter.Button(self.change_window, text="Отмена", font=("Arial", 16), width=10,
                                                command=self.__destroy_change_window)
        self.cancel_change_btn.grid(row=1, column=1, pady=4, padx=4)

        tkinter.mainloop()

    def __add_task_window(self):
        self.main_window.state("icon")
        self.add_window = tkinter.Tk()
        self.add_window.title("Add new task")


        self.description = tkinter.StringVar()
        self.priority = tkinter.StringVar()

        self.description_entry = tkinter.Entry(self.add_window, font=("Arial", 16))
        self.description_entry.grid(row=0, columnspan=2, pady=4, padx=4)

        self.priority_add_spinbox = tkinter.Spinbox(self.add_window, from_=1, to=10, font=("Arial", 16))
        self.priority_add_spinbox.grid(row=1, columnspan=2, pady=4, padx=4)

        self.task_add_btn = tkinter.Button(self.add_window, text="Добавить", font=("Arial", 16), width=10)
        self.task_add_btn.grid(row=2, column=0, pady=4, padx=4)

        self.cancel_add_btn = tkinter.Button(self.add_window, text="Отмена", font=("Arial", 16), width=10,
                                                command=self.__destroy_add_window)
        self.cancel_add_btn.grid(row=2, column=1, pady=4, padx=4)

        tkinter.mainloop()

    def __destroy_add_window(self):
        self.main_window.state("normal")
        self.add_window.destroy()

    def __destroy_change_window(self):
        self.main_window.state("normal")
        self.change_window.destroy()



