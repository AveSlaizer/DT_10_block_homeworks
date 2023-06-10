"""
Задание 1.
Создайте функцию, возвращающую список со всеми простыми числами
от 0 до 1000. Используя механизм декораторов посчитайте сколько секунд,
потребовалось для вычисления всех простых чисел. Отобразите на экран
количество секунд и простые числа
"""


def is_easy_number(number: int) -> bool:
    """
    Возвращает True если передано простое число, в противном случае False

    :param number(int): Число
    :return:
            bool
    """
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
