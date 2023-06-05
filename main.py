"""
Реализуйте архитектуру приложения, используя паттерн
«Абстрактная фабрика»
Допустим, вы решили создать программу по производству и продаже
автомобилей. Автомобили будем создавать сами. Лучшим решением будет
скупить заводы известных компаний Ford и Toyota, и продолжить выпускать
автомобили под их собственными марками, а прибыль класть себе в
карман. Будем делать автомобили с 2 типами кузова – седан и купе. Например,
японцы будут делать ToyotaSedan и ToyotaCoupe, американцы — FordSedan и
FordCoupe». Таким образом, в вашем абстрактном классе CarsFactory будут 2
метода: createSedan() и createCoupe(). Реализуйте программу и протестируйте
фабрику на примерах создания конкретных автомобилей.
"""
from abc import ABC, abstractmethod


class Car(ABC):
    pass


class Sedan(Car):
    pass


class ToyotaSedan(Sedan):
    pass


class FordSedan(Sedan):
    pass


class Coupe(Car):
    pass


class ToyotaCoupe(Coupe):
    pass


class FordCoupe(Coupe):
    pass


class CarFactory(ABC):

    @abstractmethod
    def create_sedan(self):
        raise NotImplementedError

    @abstractmethod
    def create_coupe(self):
        raise NotImplementedError


class ToyotaCarFactory(CarFactory):

    def create_sedan(self):
        return ToyotaSedan()

    def create_coupe(self):
        return ToyotaCoupe()


class FordCarFactory(CarFactory):

    def create_sedan(self):
        return FordSedan()

    def create_coupe(self):
        return FordCoupe()


def execute_application():
    toyota = ToyotaCarFactory()
    toyota_sedan = toyota.create_sedan()
    print(toyota_sedan)
    toyota_coupe = toyota.create_coupe()
    print(toyota_coupe)
    ford = FordCarFactory()
    ford_sedan = ford.create_sedan()
    print(ford_sedan)
    ford_coupe = ford.create_coupe()
    print(ford_coupe)


if __name__ == "__main__":
    execute_application()
