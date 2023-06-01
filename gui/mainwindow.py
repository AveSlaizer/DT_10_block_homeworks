import tkinter
from tkinter import messagebox
from data_structure.priority_queue import PriorityQueue, Task


class MainWindow:

    def __init__(self):
        self.queue = PriorityQueue()
        self.change_btn_state = "disabled"

        self.main_window = tkinter.Tk()
        self.main_window.title("To - Do List")

        self.main_window.columnconfigure(index=0, weight=45)
        self.main_window.columnconfigure(index=1, weight=45)

        self.main_window.rowconfigure(index=0, )

        self.actual_task = tkinter.StringVar()
        self.actual_task.set("Нет активных задач")

        self.task_label = tkinter.Label(self.main_window, textvariable=self.actual_task, font=("Arial", 16),
                                        width=40, height=10, borderwidth=3, relief="ridge", justify="left")
        self.task_label.grid(row=0, columnspan=2, sticky="wens", pady=4, padx=4)

        self.change_btn = tkinter.Button(self.main_window, text="Изменить", font=("Arial", 16),
                                         command=self.__change_actual_task_priority, state=tkinter.DISABLED)
        self.change_btn.grid(row=1, column=0, sticky="we", pady=8, padx=4)

        self.do_it_btn = tkinter.Button(self.main_window, text="Выполнить", font=("Arial", 16), state=tkinter.DISABLED,
                                        command=self.__do_task)
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

        self.change_priority_label = tkinter.Label(self.change_window, text="Приоритет: ", font=("Arial", 16))
        self.change_priority_label.grid(row=0, column=0, pady=4, padx=4)
        self.priority_change_spinbox = tkinter.Spinbox(self.change_window, from_=1, to=10, font=("Arial", 16), width=10)
        self.priority_change_spinbox.grid(row=0, column=1, pady=4, padx=4)

        self.ok_btn = tkinter.Button(self.change_window, text="OK", font=("Arial", 16), width=10,
                                     command=self.__change_priority)
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

        self.description_entry = tkinter.Text(self.add_window, font=("Arial", 16), wrap="word", width=28, height=5)
        self.description_entry.grid(row=0, columnspan=2, pady=4, padx=4)

        self.add_priority_label = tkinter.Label(self.add_window, text="Приоритет: ", font=("Arial", 16))
        self.add_priority_label.grid(row=1, column=0, pady=4, padx=4)

        self.priority_add_spinbox = tkinter.Spinbox(self.add_window, from_=1, to=10, font=("Arial", 16), width=10)
        self.priority_add_spinbox.grid(row=1, column=1, pady=4, padx=4)

        self.task_add_btn = tkinter.Button(self.add_window, text="Добавить", font=("Arial", 16), width=10,
                                           command=self.__add_new_task)
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

    def __add_new_task(self):
        description = self.description_entry.get(1.0, tkinter.END)
        priority = int(self.priority_add_spinbox.get())
        if description == "\n":
            tkinter.messagebox.showwarning("Warning", "Задание должно иметь описание!")
        else:
            task = Task(description, priority)
            self.queue.insert(task)
            text = f"Приоритет: {self.queue.peek().priority}. " \
                   f"Описание:\n{self.format_text(self.queue.peek().description)}"
            self.actual_task.set(text)
            self.change_btn["state"] = tkinter.NORMAL
            self.do_it_btn["state"] = tkinter.NORMAL
            self.__destroy_add_window()

    def __change_priority(self):
        new_priority = int(self.priority_change_spinbox.get())
        self.queue.change_actual_task_priority(new_priority)
        text = f"Приоритет: {self.queue.peek().priority}. " \
               f"Описание:\n{self.format_text(self.queue.peek().description)}"
        self.actual_task.set(text)
        self.__destroy_change_window()

    def __do_task(self):
        done_task = self.queue.delete()
        if self.queue.is_empty():
            text = "Нет активных задач"
            self.change_btn["state"] = tkinter.DISABLED
            self.do_it_btn["state"] = tkinter.DISABLED
        else:
            text = f"Приоритет: {self.queue.peek().priority}. " \
                   f"Описание:\n{self.format_text(self.queue.peek().description)}"
        self.actual_task.set(text)
        tkinter.messagebox.showinfo("Info", f"{done_task}\nЗадание выполнено")

    @staticmethod
    def format_text(text: str):
        columns = 39
        index = 1
        while index < len(text):
            if index % columns == 0:
                text = text[:index] + "\n" + text[index:]
            index += 1
        return text
