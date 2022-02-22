class StackMax:
    def __init__(self):
        self.items = []
        self.max_num = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if not self.max_num or self.max_num[-1] <= item:
            self.max_num.append(item)
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return print('error')
        if self.max_num and self.max_num[-1] == self.items[-1]:
            self.max_num.pop()
        self.items.pop()

    def get_max(self):
        if not self.max_num:
            return None
        return self.max_num[-1]


def main():
    m = int(input())
    stack = StackMax()
    for _ in range(m):
        method = input().split()
        if method[0] == 'get_max':
            print(stack.get_max())
        elif method[0] == 'pop':
            stack.pop()
        elif method[0] == 'push':
            stack.push(int(method[1]))


if __name__ == '__main__':
    main()
