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


if __name__ == '__main__':
    main()
