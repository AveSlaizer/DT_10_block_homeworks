from visitor import Visitor


class VisitorPriorityQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return ' '.join([f"/{i}/\n" for i in self.__queue])

    def is_empty(self):
        return len(self.__queue) == 0

    def insert(self, item: Visitor):
        if not isinstance(item, Visitor):
            raise TypeError(f"Недопустимый тип данных '{item.__class__.__name__}', ожидался 'User'")
        self.__queue.append(item)
        self.__queue.sort()

    def delete(self):
        return self.__queue.pop().__name
