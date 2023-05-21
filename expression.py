from data_structure.stack import Stack


class ExpressionConverter:
    operation_priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    """
Алгоритм:
1. Если не достигнут конец входной последовательности, прочитать очередную лексему.
    1.1. Если прочитан операнд (число), записать его в выходную последовательность.
    1.2. Если прочитана открывающая скобка, положить ее в стек.
    1.3. Если прочитана закрывающая скобка, вытолкнуть из стека в выходную последовательность все до открывающей скобки.
        Сами скобки уничтожаются.
    1.4. Если прочитан знак операции, вытолкнуть из стека в выходную последовательность все операции с большим либо
        равным приоритетом, а прочитанную операцию положить в стек.
2. Если достигнут конец входной последовательности, вытолкнуть все из стека в выходную последовательность и завершить 
работу.
    """

    # 5*6+(2-9) => 56*29-+
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
            elif symbol == " ":
                continue
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
        self.__infix_expression = expression
        self.__postfix_expression = ExpressionConverter.to_postfix(expression)

    @property
    def infix_expression(self):
        return self.__infix_expression

    @property
    def postfix_expression(self):
        return self.__postfix_expression

    def get_expression_value(self):
        """
        Возвращает значение выражения, записанного в постфиксной форме в поле __postfix_expression
        :return:
        """
        pass
