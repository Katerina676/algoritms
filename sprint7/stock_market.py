def main():
    n = int(input())
    prices = list(map(int, input().split()))
    res = 0
    day = 0
    buy = False
    while day < n:
        if buy:
            if day == n - 1 or prices[day] > prices[day+1]:
                buy = False
                res += prices[day]
        elif day + 1 < n and prices[day] < prices[day+1]:
            buy = True
            res -= prices[day]
        day += 1

    print(res)


if __name__ == '__main__':
    main()
