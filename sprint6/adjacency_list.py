def adjacency_list():
    n, m = map(int, input().split())
    adjacency = {v: [] for v in range(1, n+1)}
    for _ in range(m):
        v, u = map(int, input().split())
        adjacency.get(v).append(u)
    for i in range(1, n + 1):
        print(len(adjacency[i]), ' '.join(map(str, sorted(adjacency[i]))))


if __name__ == '__main__':
    adjacency_list()
