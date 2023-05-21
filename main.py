"""
Реализуйте класс стека для работы со строками. Стек должен иметь
фиксированный размер (ограничение на количество элементов, которое можно
задать при создании стека).
Реализуйте набор операций для работы со стеком:
 Добавление строки в стек;
 Удаление и возврат строки из стека;
 Подсчет количества строк в стеке;
 Проверку пустой ли стек;
 Очистку стека;
 Получение значения на вершине стека.
При старте приложения нужно отобразить меню с помощью, которого
пользователь может выбрать необходимую операцию.
"""
from stackgui import StackInitGUI


def execute_application():
    StackInitGUI()


if __name__ == "__main__":
    execute_application()
