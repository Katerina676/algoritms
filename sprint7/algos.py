def main():
    summa = int(input())
    _ = int(input())
    nom = set(list(map(int, input().split())))
    dp = [None for _ in range(summa + 1)]
    for i in range(summa + 1):
        if i in nom:
            dp[i] = 1
        else:
            min_count = float('inf')
            for j in nom:
                idx = i - j
                if idx > 0:
                    min_count = min(dp[idx] + 1, min_count)
            dp[i] = min_count
    return dp[-1]


if __name__ == '__main__':
    print(main())
