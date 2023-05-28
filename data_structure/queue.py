from data_structure.linkedList import LinkedList
from user import User


class QueueOutOfRange(Exception):
    def __init__(self, text: str):
        self.text = text


class Queue:
    def __init__(self):
        self._data = LinkedList()

    def enqueue(self, item):
        """ Добавление нового элемента item в очередь """
        self._data.add_last(item)

    def dequeue(self):
        """ Удаление и возврат очередного элемента в порядке «первым вошел, первым вышел» (FIFO) """
        return self._data.remove_first()

    def peek(self):
        """ Возврат(без удаления) очередного элемента в очереди в порядке FIFO """
        item = self._data.remove_first()
        self._data.add_first(item)
        return item

    def __len__(self):
        """ Возврат количества элементов в очереди """
        return len(self._data)

    def is_empty(self):
        """ Поверка очереди на пустоту """
        return len(self._data) == 0


class UsersQueue(Queue):

    def __init__(self, length: int):
        super().__init__()
        self.__length = length
        self._data = LinkedList()

    def enqueue(self, item: User):
        if not isinstance(item, User):
            raise TypeError(f"Недопустимый тип данных '{item.__class__.__name__}', ожидался 'User'")
        if len(self._data) < self.__length:
            self._data.add_last(item)
        else:
            raise IndexError(f"Невозможно добавить пользователя в очередь. Очередь заполнена.")

    def dequeue(self):
        if self.is_empty():
            raise IndexError(f"Невозможно удалить пользователя из очереди. Очередь пуста.")
        return self._data.remove_first()

    def peek(self):
        if self.is_empty():
            raise IndexError(f"Невозможно прочитать информацию о пользователе. Очередь пуста")
        item = self._data.remove_first()
        self._data.add_first(item)
        return item

    def info(self):
        for item in self._data.items():
            print(item)
