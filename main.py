from time import time
"""
Задание 1.
Создайте функцию, возвращающую список со всеми простыми числами
от 0 до 1000. Используя механизм декораторов посчитайте сколько секунд,
потребовалось для вычисления всех простых чисел. Отобразите на экран
количество секунд и простые числа
"""
"""
Задание 2.
Добавьте к первому заданию возможность передавать границы
диапазона для поиска всех простых чисел
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



def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        stop = time()
        print(f"Функция отработала за '{stop - start:.4f}' секунд")
        return result
    return wrapper

@timer
def make_easy_number_list(begin: int = 0, end: int = 1000) -> list[int]:
    """
    Возвращает список простых чисел из диапазона от begin до end

    :param begin(int): Начало диапазона
    :param end(int): Конец диапазона
    :return:
            (list[int]): Список простых чисел
    """
    return [i for i in range(begin, end + 1) if is_easy_number(i)]


def execute_application():
    """
    # Задание 1
    print(f"Простые числа от 1 до 1000: {make_easy_number_list()}")
    """
    """
    # Задание 2
    print(f"Простые числа от 1 до 1000: {make_easy_number_list(1, 15)}")
    """



if __name__ == "__main__":
    execute_application()
