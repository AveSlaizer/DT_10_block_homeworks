"""
Стратегия – это поведенческий паттерн проектирования, который
определяет семейство схожих алгоритмов и помещает каждый из них в
собственный класс, после чего алгоритмы можно взаимозаменять прямо во
время исполнения программы.
Вы решили написать приложение-навигатор для путешественников.
Оно должно показывать красивую и удобную карту, позволяющую с лёгкостью
ориентироваться в незнакомом городе.
Одной из самых востребованных функций являлся поиск и
прокладывание маршрутов. Пребывая в неизвестном ему городе, пользователь
должен иметь возможность указать начальную точку и пункт назначения, а
навигатор – проложит оптимальный путь.
В этом примере каждый алгоритм поиска пути переедет в свой
собственный класс. В этих классах будет определён лишь один метод,
принимающий в параметрах координаты начала и конца пути, а
возвращающий массив точек маршрута. Реализуйте класс навигатора,
который по переданной ему стратегии выполняет построение маршрута.
"""
from abc import ABC, abstractmethod


class MapCoordinate:
    pass


class BaseStrategy(ABC):

    @abstractmethod
    def build_route(self, start: MapCoordinate, finish: MapCoordinate):
        raise NotImplementedError


class WalkingStrategy(BaseStrategy):

    def build_route(self, begin: MapCoordinate, finish: MapCoordinate):
        return "Пешеходный маршрут построен"


class RoadStrategy(BaseStrategy):

    def build_route(self, start: MapCoordinate, finish: MapCoordinate):
        return "Автомобильный маршрут построен"


class PublicTransportStrategy(BaseStrategy):

    def build_route(self, start: MapCoordinate, finish: MapCoordinate):
        return "Маршрут с использованием общественного транспорта построен"


class Navigator:
    strategy: BaseStrategy

    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def build_route(self, start: MapCoordinate, finish: MapCoordinate):
        return self.strategy.build_route(start, finish)


def execute_application():
    a = MapCoordinate()
    b = MapCoordinate()
    navigator = Navigator()
    walk = WalkingStrategy()
    car = RoadStrategy()
    bus = PublicTransportStrategy()

    navigator.set_strategy(walk)
    print(navigator.build_route(a, b))

    navigator.set_strategy(car)
    print(navigator.build_route(a, b))

    navigator.set_strategy(bus)
    print(navigator.build_route(a, b))


if __name__ == "__main__":
    execute_application()
