class Visitor:

    def __init__(self, name: str, priority: int):
        self.__name = name
        self.__priority = priority

    @property
    def name(self):
        return self.__name

    @property
    def priority(self):
        return self.__priority

    def __str__(self):
        return f"имя: {self.__name}, приоритет: {self.__priority}"

    def __lt__(self, other):
        if isinstance(other, Visitor):
            return self.__priority < other.__priority
        raise TypeError(f"Невозможно сравнить '{self.__class__.__name__}' и '{other.__class__.__name__}'")

    def __gt__(self, other):
        if isinstance(other, Visitor):
            return self.__priority > other.__priority
        raise TypeError(f"Невозможно сравнить '{self.__class__.__name__}' и '{other.__class__.__name__}'")
