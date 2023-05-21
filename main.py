"""
Задание 1.
Перевести выражение из инфиксной формы в постфиксную форму
записи.
"""
from expression import Expression, ExpressionConverter


def execute_application():
    """expression = "5*6+(2-9)"
    print(Expression(expression).postfix_expression)"""
    expression = "-5*(-6)+(2-(-9))"
    print(ExpressionConverter.normalize_infix_expression(expression))


if __name__ == "__main__":
    execute_application()
