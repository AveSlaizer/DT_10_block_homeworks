"""
Паттерн «Заместитель».
Представьте себе дверь, которую можно открыть лишь картой доступа
либо нажатием кнопки. Главная функциональность двери — это ее открытие,
а заместитель, который добавлен поверх (кнопка, карт-ридер), отвечает за
безопасность и расширяет функциональность.
Создайте абстрактный класс Door с методами open() и close().
Реализуйте наследника этого класса LaboratoryDoor, который реализует
методы этого класса.
Также у нас будет существовать заместитель Security, обеспечивающий
защиту любых дверей.
Реализуйте класс заместитель SecurityDoor, который в конструкторе
принимает объект класса Door. Класс заместителя должен реализовывать те
же методы что и наследники класса Door. В методе open() необходимо
выполнить аутентификацию. Аутентификацию реализовать отдельным
методом, который принимает пароль и определяет подходит он к двери или
нет. Таким образом к оригинальной двери мы накладываем логику проверки
доступа.
"""
from abc import ABC, abstractmethod


class WrongPassword(Exception):
    def __init__(self, text):
        self.text = text


class Door(ABC):

    @abstractmethod
    def open(self, *args):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError


class LaboratoryDoor(Door):

    def open(self):
        print("Дверь лаборатории открыта")

    def close(self):
        print("Дверь лаборатории закрыта")


class SecurityDoor(Door):
    __password = "1234"

    def __init__(self, door: Door):
        self.__door = door

    def __authentication(self, password: str):
        if password != self.__password:
            raise WrongPassword("Не правильный пароль!")

    def set_password(self, new_password: str):
        self.__password = new_password

    def open(self, password: str):
        self.__authentication(password)
        self.__door.open()

    def close(self):
        self.__door.close()


def execute_application():
    password = "1234"
    door = SecurityDoor(LaboratoryDoor())
    door.open(password)
    door.set_password("1231")
    door.open(password)



if __name__ == "__main__":
    execute_application()
