"""
Задание 1.
Перевести выражение из инфиксной формы в постфиксную форму
записи.
"""
from expression import Expression


def execute_application():
    a_string = "(1 + 4) / (4 + (-3))"
    expression = Expression(a_string)

    print(expression.postfix_expression)
    print(eval(a_string))
    print(expression.get_expression_value())


if __name__ == "__main__":
    execute_application()
