# -- ПРИНЦИП РАБОТЫ --
# Реализация двусторонней очереди(deque) на основе
# круговой очереди(кольцевой массив) ограниченного размера n.
# Реализованы методы такие как: pop_back, pop_front удаление из конца
# и начала очереди и возврат удаленного элемента и
# push_back, push_front добавление элемента в конец и
# начала очереди.Когда элемент добавляется в начало очереди,
# указатель начала сдвигается на элемент влево, когда элемент
# добавляется в конец очереди, указатель конца сдвигается вправо.
# Удаление элемента с его возвратом происходит из указателя начала
# выбирается элемент и указатель уходит на элемент вправо.
# Аналогично и с обратной стороны, указатель конца смещается
# на единицу влево после удаления элемента.
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Дек имеет фиксированное количество памяти.Метод is_full контролирует переполнение дека,
# чтобы элементы не перезаписывали друг друга. Двусторонняя очередь действует по принципам LIFO
# и FIFO с помощью реализованны методов ,которые обеспечивают удаление и вставку и в
# начало и конец очереди.
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Временная сложность операция вставки и удаления константное - O(1),
# за счет того что элементы не сдвигаются к началу при удалении из начала массива
# и не выделяется лишняя память.
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Пространственная сложность - использование пространства, достигаемое массивом,
# зависит от коэффициента загрузки. Если в очереди n элементов,
# значит она занимает O(n) памяти.
# id 64044582

class IsEmptyError(Exception):
    pass


class IsFullError(Exception):
    pass


class Deque:
    def __init__(self, m: int):
        self.queue = [None] * m
        self.max_size = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def push_back(self, value: int):
        if self.is_full():
            raise IsFullError
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value: int):
        if self.is_full():
            raise IsFullError
        self.queue[self.head - 1] = value
        self.head = (self.head - 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IsEmptyError
        value = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value

    def pop_front(self):
        if self.is_empty():
            raise IsEmptyError
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value


def main():
    n = int(input())
    m = int(input())
    deque = Deque(m)
    for _ in range(n):
        method, *args = input().split(' ')
        try:
            value = getattr(deque, method)(*args)
            if value:
                print(value)
        except (IsEmptyError, IsFullError):
            print('error')


if __name__ == '__main__':
    main()
