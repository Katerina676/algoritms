# --- ПРИНЦИП РАБОТЫ ---
# Реализована структура данных хеш-таблица без использования встроенной структуры dict с использованием массива.
# По условию задачи мы знаем количество запросов и делаем массив размером с количеством запросов.HashMap поддерживает
# операции по удалению, вставке и поиску по ключу.
# --- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ ---
# Мы вычисляем индекс корзины используя хеш-функцию  x = h(k) mod M.В качестве модуля мы берем максимальный размер
# массива.В качестве ключа передается id и потом вычисляется по формуле выше мод от числа.Разрешение коллизий мы
#  производим методом открытой адресации, поэтому будем хешировать ключ и двигаться по
# массиву, если ячейка по хешированному ключу уже занята, двигемся пока не встретим пустую или удаленную ячейку.
# Хеш-функция по модулю всегда будет даввать одно и то же значение
#
# Для вставки элемента ищем свободное место которое либо None либо deleted, или если там лежит уже этот ключ,
# то обновляем значение. Для того чтобы найти по ключу значение мы проверяем есть ли на этом месте такой ключ если есть
# возвращаем значение, если нет то возвращаем None. А после удаления элемента по ключу помечаем это место как deleted.
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
# Сложность алгоритма в лучшем и среднем случае О(1) при вставке и удалении и поиске по ключу.В худшем случае О(n)
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
# Алгоритм будет занимать О(n) памяти так как в массиве n-элементов
# id 64523483

class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_key(self, key, put=False):
        hash_key = hash(key) % self.size
        table = self.table[hash_key]
        index = 0
        while not (table is None or put and table == 'deleted' or table != 'deleted' and table[0] == key) \
                and index < self.size:
            hash_key = (hash_key+index) % self.size
            table = self.table[hash_key]
            index += 1
        if index < self.size:
            return hash_key
        else:
            return None

    def get(self, key):
        table = self.table[self.hash_key(key)]
        if table is None:
            return None
        if table[0] == key:
            return table[1]

    def put(self, key, value):
        table = self.hash_key(key, True)
        self.table[table] = [key, value]

    def delete(self, key):
        key = self.hash_key(key)
        if key is None:
            return None
        table = self.table[key]
        if table is None:
            return None
        self.table[key] = 'deleted'
        return table[1]


def main():
    n = int(input())
    hash_map = HashMap(n)
    for _ in range(n):
        args = input().strip().split()

        if args[0] == 'get':
            print(hash_map.get(int(args[1])))
        elif args[0] == 'put':
            hash_map.put(int(args[1]), int(args[2]))
        elif args[0] == 'delete':
            print(hash_map.delete(int(args[1])))


if __name__ == '__main__':
    main()
