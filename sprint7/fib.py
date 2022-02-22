def main():
    n = int(input())
    if n == 0:
        return 1
    mod = 10 ** 9 + 7
    res = [None for _ in range(n + 1)]
    res[0] = res[1] = 1
    for i in range(2, n + 1):
        res[i] = (res[i - 1] + res[i - 2]) % mod
    return res[n]


if __name__ == '__main__':
    print(main())
