def main():
    m = int(input())
    n = int(input())
    heaps = []
    for i in range(n):
        price, weight = map(int, input().strip().split())
        heaps.append([price, weight])
    heaps.sort(reverse=True)
    res = 0
    i = 0
    while m > 0 and i < n:
        w = min(heaps[i][1], m)
        m -= w
        res += heaps[i][0] * w
        i += 1
    print(res)


if __name__ == '__main__':
    main()
