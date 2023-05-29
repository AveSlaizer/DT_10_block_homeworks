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
