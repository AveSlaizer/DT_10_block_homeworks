import tkinter
from tkinter import messagebox
from data_structure.stringstack import StringStack

class StackGUI:

    def __init__(self, value):
        self.stack = StringStack(value)

        self.main_window = tkinter.Tk()
        self.main_window.title("Stack controller")

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.entry_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.quit_frame = tkinter.Frame(self.main_window)

        # Top frame
        self.size_label = tkinter.Label(self.top_frame, text="       Количество элементов: ")
        self.size = tkinter.StringVar()
        self.size.set("0")
        self.show_size = tkinter.Label(self.top_frame, textvariable=self.size,
                                       width=20, borderwidth="1", relief="solid")

        # Middle frame
        self.last_item_label = tkinter.Label(self.middle_frame, text="Последний элемент стэка: ")
        self.last_item = tkinter.StringVar()
        self.last_item.set("Пусто")
        self.show_last_item = tkinter.Label(self.middle_frame, textvariable=self.last_item,
                                            width=20, borderwidth="1", relief="solid")

        # Entry frame
        self.entry_label = tkinter.Label(self.entry_frame, text="Введите элемент: ")
        self.value_entry = tkinter.Entry(self.entry_frame, width=20)
        self.add_button = tkinter.Button(self.entry_frame, text="Добавить", command=self.__add_item)

        # Button frame
        self.del_item_btn = tkinter.Button(self.button_frame, text="Удалить", command=self.__del_item)
        self.clear_stack_btn = tkinter.Button(self.button_frame, text="Очистить", command=self.__clear_stack)

        # Quit frame
        self.quit_btn = tkinter.Button(self.quit_frame, text="Выход", command=self.main_window.destroy)

        self.size_label.pack(side="left")
        self.show_size.pack(side="left")

        self.top_frame.pack(padx=10, pady=5)

        self.last_item_label.pack(side="left")
        self.show_last_item.pack(side="left")

        self.middle_frame.pack(padx=10, pady=5)

        self.entry_label.pack(side="left")
        self.value_entry.pack(side="left")
        self.add_button.pack(side="left")

        self.entry_frame.pack(padx=10, pady=5)

        self.del_item_btn.pack(side="left", padx=10)
        self.clear_stack_btn.pack(side="left", padx=10)

        self.button_frame.pack(padx=10, pady=5)

        self.quit_btn.pack(padx=10, pady=5)

        self.quit_frame.pack(padx=10, pady=5)

        tkinter.mainloop()

    def __add_item(self):
        value = self.value_entry.get()
        if value:
            try:
                self.stack.push(value)
                self.size.set(str(len(self.stack)))
                self.last_item.set(self.stack.peek())
                self.value_entry.delete(0, tkinter.END)
            except Exception as e:
                tkinter.messagebox.showerror("Ошибка!", e)
                self.value_entry.delete(0, tkinter.END)

        else:
            tkinter.messagebox.showerror("Ошибка!", "Введите текст для добавления!")

    def __del_item(self):
        try:
            deleted_item = self.stack.pop()
            self.size.set(str(len(self.stack)))
            self.last_item.set(self.stack.peek())
            tkinter.messagebox.showinfo("Сообщение", f"Элемент '{deleted_item}' успешно удален")
        except Exception as e:
            tkinter.messagebox.showerror("Ошибка!", e)

    def __clear_stack(self):
        self.stack.clear()
        self.size.set(str(len(self.stack)))
        self.last_item.set(self.stack.peek())
        tkinter.messagebox.showinfo("Сообщение", "Все элементы стэка удалены")


class StackInitGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title("Создание стэка")
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="Введите максимальное количество элементов стэка:")
        self.size_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.size_entry.pack(side="left")

        self.return_value_btn = tkinter.Button(self.bottom_frame,
                                               text="Создать",
                                               command=self.get_value)
        self.quit_btn = tkinter.Button(self.bottom_frame,
                                       text="Выход",
                                       command=self.main_window.destroy)

        self.return_value_btn.pack(side="left")
        self.quit_btn.pack(side="left")

        self.top_frame.pack(padx=10, pady=5)
        self.bottom_frame.pack(padx=10, pady=5)

        tkinter.mainloop()


    def get_value(self):
        try:
            value = int(self.size_entry.get())
            assert value >= 1, "Максимальный размер стэка не может быть меньше '1'"
            self.main_window.destroy()
            StackGUI(value)
        except TypeError as e:
            tkinter.messagebox.showerror("Ошибка!", e)
            self.size_entry.delete(0, tkinter.END)
        except AssertionError as e:
            tkinter.messagebox.showerror("Ошибка!", e)
            self.size_entry.delete(0, tkinter.END)
