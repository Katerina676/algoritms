WHITE = 0
GRAY = 1
BLACK = 2


def dfs(start, graph, colors, tin, tout):
    stack = [start]
    time = -1
    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == WHITE:
            time += 1
            tin[v] = time
            colors[v] = GRAY
            stack.append(v)
            for i in sorted(graph[v], reverse=True):
                if colors[i] == WHITE:
                    stack.append(i)
        elif colors[v] == GRAY:
            time += 1
            tout[v] = time
            colors[v] = BLACK


def main():
    n, m = map(int, input().split())
    adjacency_list = {v: [] for v in range(1, n + 1)}
    colors = {(n + 1): WHITE for n in range(n)}
    tin = [0 for n in range(n + 1)]
    tout = [0 for n in range(n + 1)]
    for _ in range(m):
        v, u = map(int, input().split())
        adjacency_list[v].append(u)
    start = 1
    dfs(start, adjacency_list, colors, tin, tout)
    for i in range(1, n + 1):
        print(f'{tin[i]} {tout[i]}')


if __name__ == '__main__':
    main()
