from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2


def bfs(start, graph, colors):
    deque_graph = deque([start])
    colors[start] = GRAY
    prev = {}
    road = {start: 1}

    while len(deque_graph) > 0:
        v = deque_graph.pop()
        yield v
        for i in sorted(graph[v]):
            if colors[i] == WHITE:
                road[i] = road[v] + 1
                prev[i] = v
                colors[i] = GRAY
                deque_graph.appendleft(i)
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
    print(*bfs(start, adjacency_list, colors))


if __name__ == '__main__':
    main()
