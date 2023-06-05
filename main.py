"""
Задание 1
Реализуйте архитектуру приложения, используя паттерн «Фабричный
метод».
Представьте, что вы создали программу управления доставкой еды. В
программе в качестве единственного средства доставки используется электросамокат.
Ваши курьеры на электро-самокатах развозят еду из пункта А в
пункт Б. Все просто.
Программа набирает популярность и ваш бизнес растет. Парк самокатов
ограничен и вы решаете подключить к вашей системе доставки велосипеды и
автомобили. Вам важно знать когда будет доставлена еда и сколько единиц
продуктов может забрать курьер. У транспортных средств разная скорость и
вместимость.
"""
from abc import ABC, abstractmethod

"""
class Transport(ABC):

    @abstractmethod
    def get_middle_speed(self):
        raise NotImplementedError

    @abstractmethod
    def get_max_weight(self):
        raise NotImplementedError


class Scooter(Transport):
    __middle_speed = 8
    __max_weight = 4

    def get_middle_speed(self):
        return self.__middle_speed

    def get_max_weight(self):
        return self.__max_weight

    def __str__(self):
        return f"Максимальный груз: {self.__max_weight} кг, средняя скорость: {self.__middle_speed}"


class Bike(Transport):
    __middle_speed = 12
    __max_weight = 6

    def get_middle_speed(self):
        return self.__middle_speed

    def get_max_weight(self):
        return self.__max_weight

    def __str__(self):
        return f"Максимальный груз: {self.__max_weight} кг, средняя скорость: {self.__middle_speed}"


class Car(Transport):
    __middle_speed = 25
    __max_weight = 50

    def get_middle_speed(self):
        return self.__middle_speed

    def get_max_weight(self):
        return self.__max_weight

    def __str__(self):
        return f"Максимальный груз: {self.__max_weight} кг, средняя скорость: {self.__middle_speed}"


class Deliver(ABC):

    @abstractmethod
    def create_transport(self):
        raise NotImplementedError


class ScooterDeliver(Deliver):

    def create_transport(self):
        return Scooter()


class BikeDeliver(Deliver):

    def create_transport(self):
        return Bike()


class CarDeliver(Deliver):

    def create_transport(self):
        return Car()
"""
"""
Задание 2.
Реализуйте архитектуру приложения, используя паттерн «Строитель».
Чтобы построить стандартный дом, нужно поставить 4 стены,
установить двери, вставить пару окон и постелить крышу. Но что, если вы
хотите дом побольше, посветлее, с бассейном, садом и прочим добром?
Паттерн предлагает разбить процесс конструирования объекта на
отдельные шаги (например, построить стены, вставить двери и т.д.) Чтобы
создать объект, вам нужно поочерёдно вызывать методы строителя. Причём
не нужно запускать все шаги, а только те, что нужны для производства
объекта определённой конфигурации.
"""


class House:
    def __init__(self):
        self.walls = 0
        self.doors = 0
        self.windows = 0
        self.swimming_pool = False
        self.garden = False
        self.garage = False


class Builder(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def set_walls(self, value):
        raise NotImplementedError

    @abstractmethod
    def set_doors(self, value):
        raise NotImplementedError

    @abstractmethod
    def set_windows(self, value):
        raise NotImplementedError

    @abstractmethod
    def set_swimming_pool(self):
        raise NotImplementedError

    @abstractmethod
    def set_garden(self):
        raise NotImplementedError

    @abstractmethod
    def set_garage(self):
        raise NotImplementedError

    @abstractmethod
    def get_house(self):
        raise NotImplementedError


class BrickHouseBuilder(Builder):
    __house: House

    def create(self):
        self.__house = House()

    def set_walls(self, value):
        self.__house.walls = value

    def set_doors(self, value):
        self.__house.doors = value

    def set_windows(self, value):
        self.__house.windows = value

    def set_swimming_pool(self):
        self.__house.swimming_pool = True

    def set_garden(self):
        self.__house.garden = True

    def set_garage(self):
        self.__house.garage = True

    def get_house(self):
        return self.__house


def execute_application():
    builder = BrickHouseBuilder()
    builder.create()
    builder.set_walls(4)
    builder.set_doors(2)
    builder.set_windows(4)
    builder.set_garage()
    house = builder.get_house()
    print(house.__dict__)


if __name__ == "__main__":
    execute_application()
