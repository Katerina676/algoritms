class StackMax:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return print('error')
        self.items.pop()

    def get_max(self):
        if self.is_empty():
            return None
        max_num = max(self.items)
        return max_num


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