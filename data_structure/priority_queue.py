class Task:
    def __init__(self, description: str, priority: int):
        self.__description = description
        self.__priority = priority

    @property
    def description(self):
        return self.__description

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority



class PriorityQueue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.__queue])

    def is_empty(self):
        return not self.__queue

    def peek(self):
        if not self.is_empty():
            return self.__queue[-1]
        raise IndexError("Нет активных задач")

    def insert(self, task: Task):
        self.__queue.insert(0, task)
        self.__queue.sort()

    def delete(self):
        if not self.is_empty():
            return self.__queue.pop().description
        raise IndexError("Отсутствует актуальная задача")

    def change_actual_task_priority(self, priority: int):
        if not self.is_empty():
            self.__queue[-1].priority = priority
            self.__queue.sort()
        raise IndexError("Отсутствует актуальная задача")