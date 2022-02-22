def distance():

    a = list(input().strip())
    b = list(input().strip())
    n, m = len(a), len(b)

    if m == 0 or n == 0:
        return max(n, m)

    dp = [[i] + [0] * m for i in range(n + 1)]
    dp[0] = list(range(0, m + 1))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    return dp[n][m]


if __name__ == "__main__":
    print(distance())
