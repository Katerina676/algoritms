def main():
    n, k = map(int, input().split())
    dp = [0, 1] + [0] * (n - 1)
    mod = 10 ** 9 + 7
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            if i >= j:
                dp[i] += dp[i - j]
        dp[i] %= mod
    print(dp[n])


if __name__ == '__main__':
    main()
