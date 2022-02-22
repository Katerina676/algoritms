# -- ПРИНЦИП РАБОТЫ --
# Реализация калькулятора с польской нотацией на основе структуры данных -стек.
# Происходит итерация , которая кладет число в конец стека, либо извлекает
# два последних числа, на них выполняется операция и результат кладется в конец
# стека.
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# За счет того что стек работает по методу LIFO условия польской нотации о
# порядке операция сохраняются.
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Временная сложность операция вставки и удаления  из стека константное - O(1),
# а итерация по элементам занимает O(n) времени.
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Сложность зависит от количества элементов в стеке - n,
# значит она занимает O(n) памяти.
# id 64045999
# РЕШЕНИЕ № 1

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()


def calculator():
    stack = Stack()
    operands = input()
    for i in operands.split():
        if i == '+':
            x, y = stack.pop(), stack.pop()
            stack.push(x + y)
        elif i == "-":
            x, y = stack.pop(), stack.pop()
            stack.push(y - x)
        elif i == "*":
            x, y = stack.pop(), stack.pop()
            stack.push(x * y)
        elif i == "/":
            x, y = stack.pop(), stack.pop()
            stack.push(y // x)
        else:
            stack.push(int(i))
    return stack.pop()


if __name__ == '__main__':
    print(calculator())
