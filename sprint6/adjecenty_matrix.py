def adjecenty_matrix():
    n, m = map(int, input().split())
    matrix = [[0] * n for _ in range(n)]
    for _ in range(m):
        i, j = map(int, input().split())
        matrix[i - 1][j - 1] = 1
    for i in matrix:
        print(' '.join(map(str, i)))


if __name__ == '__main__':
    adjecenty_matrix()
