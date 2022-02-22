WHITE = 0
GRAY = 1
BLACK = 2


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def dfs(start, graph, colors):
    stack = Stack()
    stack.push(start)
    while stack.size() > 0:
        v = stack.pop()
        if colors[v] == WHITE:
            yield v
            colors[v] = GRAY
            stack.push(v)
            for i in sorted(graph[v], reverse=True):
                if colors[i] == WHITE:
                    stack.push(i)
        elif colors[v] == GRAY:
            colors[v] = BLACK


def main():
    n, m = map(int, input().split())
    adjacency_list = {v: [] for v in range(1, n + 1)}
    colors = {(n + 1): WHITE for n in range(n)}
    for _ in range(m):
        v, u = map(int, input().split())
        adjacency_list[v].append(u)
        adjacency_list[u].append(v)
    start = int(input().strip())
    print(*dfs(start, adjacency_list, colors))


if __name__ == '__main__':
    main()
