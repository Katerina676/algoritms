def main():
    n = int(input())
    time = []
    for _ in range(n):
        start, end = map(float, input().strip().split())
        time.append([start, end])
    time.sort(key=lambda x: (x[1], x[0]))
    res = []
    res.append(time[0])
    for i in range(1, len(time)):
        if time[i][0] >= res[-1][1]:
            res.append(time[i])
    print(len(res))
    for i in res:
        print(*i)


if __name__ == '__main__':
    main()
