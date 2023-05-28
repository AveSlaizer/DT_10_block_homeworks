"""
Создайте класс очереди с приоритетами для работы с объектами
определенного класса (реализуйте на своё усмотрение). Требуется создать
реализации для операций над элементами очереди:
is_empty — проверка очереди на пустоту.
insert_with_priority—добавление элемента c приоритетом в очередь.
pull_highest_priority_element—удаление элемента c высшим
приоритетом из очереди.
peek—возврат самого большого по приоритету элемента. Обращаем
ваше внимание,что элемент не удаляется из очереди.
show—отображение всех элементов очереди на экран. При показе
элемента также необходимо отображать приоритет.
При старте приложения нужно отобразить меню с помощью, которого
пользователь может выбрать необходимую операцию.
"""
from data_structure.priority_queue import VisitorPriorityQueue
from visitor import Visitor

def show_menu():
    print(f"Выберите действие:\n"
          f"1 > Добавление посетителя в очередь\n"
          f"2 > Вызвать посетителя из очереди\n"
          f"3 > Вывести на экран данные следующего в очереди посетителя\n"
          f"4 > Отобразить статус очереди\n"
          f"5 > Вывод данных всех посетителей на экран\n"
          f"0 > Завершение работы программы\n")
def execute_application():
    queue = VisitorPriorityQueue()
    while True:
        show_menu()
        main_action = input(" >>> ")
        if main_action == "1":
            name = input("Напишите, как обращаться к посетителю: ")
            business = input("Выберите цель визита:\n"
                             "1 > Получение кредита\n"
                             "2 > Оплата коммунальных услуг\n"
                             "3 > Внести/снять наличные на счет\n"
                             " >>> ")
            if business == "1":
                priority = 3
            elif business == "2":
                priority = 2
            elif business == "3":
                priority = 1
            else:
                print("Не удалось определить цель визита")
                continue
            visitor = Visitor(name, priority)
            queue.insert_with_priority(visitor)
            print(f"{visitor} добавлен в очередь")
        elif main_action == "2":
            try:
                next_visitor = queue.pull_highest_priority_element()
                print(f"Посетитель '{next_visitor}' вызван к освободившемуся сотруднику")
            except IndexError:
                print("Невозможно вызвать посетителя. Очередь пуста")
        elif main_action == "3":
            try:
                print(f"Следующим будет вызван: {queue.peek()}")
            except IndexError:
                print("Невозможно отобразить следующего пользователя. Очередь пуста")
        elif main_action == "4":
            if queue.is_empty():
                print("Очередь пуста")
            else:
                print(f"В очереди {len(queue)} посетителей")
        elif main_action == "5":
            if queue.is_empty():
                print("Очередь пуста")
            else:
                queue.show()
        elif main_action == "0":
            print("Завершение работы программы")
            break
        else:
            print("Выбрано недопустимое действие. Повторите ввод")


if __name__ == "__main__":
    execute_application()
