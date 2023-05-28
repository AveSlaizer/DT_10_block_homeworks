from visitor import Visitor


class VisitorPriorityQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return ' '.join([f"/{i}/\n" for i in self.__queue])

    def is_empty(self):
        """ проверка очереди на пустоту """
        return len(self.__queue) == 0

    def insert_with_priority(self, item: Visitor):
        """ добавление элемента c приоритетом в очередь """
        if not isinstance(item, Visitor):
            raise TypeError(f"Недопустимый тип данных '{item.__class__.__name__}', ожидался 'User'")
        self.__queue.insert(0, item)
        self.__queue.sort()

    def peek(self):
        """ возврат самого большого по приоритету элемента """
        return self.__queue[-1]

    def pull_highest_priority_element(self):
        """ удаление элемента c высшим приоритетом из очереди """
        return self.__queue.pop().name

    def show(self):
        """ отображение всех элементов очереди на экран """
        for visitor in self.__queue:
            print(visitor)

    def __len__(self):
        return len(self.__queue)
