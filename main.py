"""
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


def execute_application():

    scooter_deliver = ScooterDeliver()
    scooter = scooter_deliver.create_transport()
    print(scooter)
    print(scooter.get_max_weight(), scooter.get_middle_speed())

    bike_deliver = BikeDeliver()
    bike = bike_deliver.create_transport()
    print(bike)
    print(bike.get_max_weight(), bike.get_middle_speed())

    car_deliver = CarDeliver()
    car = car_deliver.create_transport()
    print(car)
    print(car.get_max_weight(), car.get_middle_speed())


if __name__ == "__main__":
    execute_application()
