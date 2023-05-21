class StringStack:

    def __init__(self, lenght: int = 10):
        self.__data = []
        self.__lenght = self.__lenght_validator(lenght)

    def __lenght_validator(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Недопустимый тип данных '{value.__class__.__name__}', ожидался 'int'")
        if value < 1:
            raise ValueError(f"Максимальный размер стэка не может быть меньше '1'")
        return value

    def __item_validator(self, item):
        if not isinstance(item, str):
            raise TypeError(f"Недопустимый тип данных '{item.__class__.__name__}', ожидался 'str'")
        return item

    def push(self, item):
        self.__data.append(self.__item_validator(item))

    def pop(self):
        if self.is_empty():
            raise Exception(f"Невозможно извлечь элемент. Стэк пуст")
        return self.__data.pop()

    def peek(self):
        if self.is_empty():
            raise Exception(f"Невозможно прочитать элемент. Стэк пуст")
        return self.__data[-1]

    def __len__(self):
        return len(self.__data)

    def is_empty(self):
        return not self.__data

    def clear(self):
        self.__data = []
