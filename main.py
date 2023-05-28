"""
Реализуйте класс очереди для работы с пользователями (каждому
пользователю соответствует пара логин и пароль) на основе связного списка.
Очередь должна иметь фиксированный размер (ограничение на количество
элементов, которое можно задать при создании очереди).
Реализуйте набор операций для работы с очередью:
 Добавление пользователя в очередь;
 Удаление и возврат пользователя из очереди;
 Подсчет количества пользователей в очереди;
 Проверку пустая ли очередь;
 Вывод всех пользователей из очереди на экран.
При старте приложения нужно отобразить меню с помощью, которого
пользователь может выбрать необходимую операцию.
"""
from data_structure.queue import UsersQueue
from user import User


def show_menu():
    """
    Печатает меню программы в консоль
    """
    print(f"Выберите действие:\n"
          f"1 > Добавить пользователя в очередь.\n"
          f"2 > Удаление и возврат пользователя из очереди.\n"
          f"3 > Показать количество пользователей в очереди.\n"
          f"4 > Проверка, пустая ли очередь.\n"
          f"5 > Вывод всех пользователей из очереди на экран.\n"
          f"0 > Завершение программы.")


def execute_application():
    while True:
        try:
            queue_lenght = int(input("Введите количество мест в очереди: "))
            user_queue = UsersQueue(queue_lenght)
            break
        except ValueError:
            print("Недопустимый тип данных. Количество мест должно быть целым числом!")

    while True:
        show_menu()
        main_action = input(" >>> ")
        if main_action == "1":
            try:
                assert len(user_queue) < queue_lenght, "Невозможно добавить пользователя в очередь. Очередь заполнена."
                user = User(
                    input("Введите логин пользователя: "),
                    input("Введите пароль пользователя: ")
                )

                user_queue.enqueue(user)
                print(f"Пользователь {user} добавлен в очередь")
            except IndexError as e:
                print(e)
            except AssertionError as e:
                print(e)
        elif main_action == "2":
            try:
                temp_user = user_queue.dequeue()
                print(f"Пользователь {temp_user} вышел из очереди")
            except IndexError as e:
                print(e)
        elif main_action == "3":
            print(f"В очереди {len(user_queue)} пользователей")
        elif main_action == "4":
            if user_queue.is_empty():
                print("Очередь пуста")
            else:
                print("В очереди есть пользователи")
        elif main_action == "5":
            if user_queue.is_empty():
                print("Очередь пуста")
            else:
                print("в очереди находятся следующие пользователи:")
                user_queue.info()
        elif main_action == "0":
            print("Завершение работы программы.")
            break
        else:
            print("Выбрано недопустимое действие! Повторите ввод.")




if __name__ == "__main__":
    execute_application()
