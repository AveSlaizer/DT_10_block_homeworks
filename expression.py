from data_structure.stack import Stack


class ExpressionConverter:
    operation_priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    @staticmethod
    def __normalize_infix_expression(expression: str) -> str:
        """
        Метод, который учитывает отрицательные значения и приводит инфиксную
        запись выражения к виду пригодному для перевода в постфиксную запись
        :param expression(str): Выражение
        :return:
                result(str): Нормализованное выражение
        """
        if expression[0] == "-":
            expression = "0" + expression
        if "(-" in expression:
            expression = expression.replace("(-", "(0-")
        return expression

    @staticmethod
    def __convert_expression_to_list(expression: str) -> list:
        """
        Конвертирует выражание из строки в список из чисел и знаков операций
        :param expression(str): Строка с выражением
        :return:
                result(list): Список из чисел и знаков операций
        """
        temp_str = ""
        result = []
        for index, symbol in enumerate(expression):
            if symbol.isalnum():
                temp_str += symbol
            else:
                if temp_str:
                    result.append(int(temp_str))
                    temp_str = ""
                result.append(symbol)
        if temp_str:
            result.append(int(temp_str))
        return result

    @staticmethod
    def to_postfix(expression: str) -> list:
        """
        Конвертирует строку с выражением в список из чисел и знаковы операций в постфиксной форме записи

        :param expression(str): Выражение
        :return:
                postfix(list): Список из чисел и знаков операций
        """
        stack = Stack()
        postfix = []
        expression = expression.replace(" ", "")
        expression = ExpressionConverter.__normalize_infix_expression(expression)
        infix = ExpressionConverter.__convert_expression_to_list(expression)

        for item in infix:
            if isinstance(item, int):
                postfix.append(item)
            elif item == "(":
                stack.push(item)
            elif item == ")":
                while stack.peek() != "(":
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while not stack.is_empty() and ExpressionConverter.operation_priority[stack.peek()] >= \
                        ExpressionConverter.operation_priority[item]:
                    postfix.append(stack.pop())
                stack.push(item)
        while not stack.is_empty():
            postfix.append(stack.pop())
        return postfix


class Expression:

    def __init__(self, expression: str):
        self.__infix_expression = self.__brackets_validator(expression)
        self.__postfix_expression = ExpressionConverter.to_postfix(expression)

    @property
    def infix_expression(self):
        return self.__infix_expression

    @property
    def postfix_expression(self):
        return self.__postfix_expression

    def __brackets_validator(self, expression):
        """
        Проверяет, правильно ли расставлены скобки
        внутри инфиксной записи арифметического выражения
        :return:
                bool
        """
        brackets = {
            '(': ')'
        }
        s = Stack()
        for symbol in expression:
            if symbol in brackets.keys():
                s.push(symbol)
            elif not s.is_empty() and symbol == brackets[s.peek()]:
                s.pop()
            elif symbol in brackets.values():
                raise Exception("В выражении не верно расставлены скобки")
            else:
                continue
                #raise Exception("В выражении не верно расставлены скобки")

        if s.is_empty():
            return expression
        raise Exception("В выражении не верно расставлены скобки")

    def get_expression_value(self):
        """
        Возвращает значение выражения, записанного в постфиксной форме в поле __postfix_expression
        :return:
        """
        pass
