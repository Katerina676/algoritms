class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_key(self, key):
        return hash(key) % self.size

    def get(self, key):
        table = self.table[self.hash_key(key)]
        if table is None:
            return None
        key = table[1] if table[0] == key else None
        return key

    def put(self, key, value):
        table = self.hash_key(key)
        if self.table[table] is None or self.table[table] == 'deleted':
            self.table[table] = [key, value]
        if self.table[table][0] == key and self.table[table][1] != value:
            self.table[table] = [key, value]
        self.table[table] = [key, value]

    def delete(self, key):
        keys = self.hash_key(key)
        if keys is None:
            return None
        table = self.table[keys]
        if table is None:
            return None
        if table[0] == key:
            self.table[keys] = 'deleted'
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

