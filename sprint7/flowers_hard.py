def main():
    n, m = map(int, input().split())

    dp = [[0] * m for _ in range(n)]
    field = []
    for _ in range(n):
        flowers = [int(x) for x in list(input())]
        field.append(flowers)

    for i in range(n - 1, -1, -1):
        for j in range(m):
            if j - 1 < 0:
                l_val = 0
            else:
                l_val = dp[i][j - 1]
            if i + 1 > n - 1:
                d_val = 0
            else:
                d_val = dp[i + 1][j]
            dp[i][j] = max(l_val, d_val) + field[i][j]
    print(dp[0][m-1])

    path = []
    i = 0
    j = m - 1
    while i != n - 1 or j != 0:
        if i == n - 1:
            down_value = -1
        else:
            down_value = dp[i + 1][j]

        if j - 1 == -1:
            left_value = -1
        else:
            left_value = dp[i][j - 1]

        if down_value > left_value:
            path.append('U')
            i += 1
        else:
            path.append('R')
            j -= 1

    path.reverse()
    print(''.join(path))


if __name__ == '__main__':
    main()
