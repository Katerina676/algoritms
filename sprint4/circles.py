def circles(arr):
    dict_circles = {}
    for i in arr:
        if i not in dict_circles:
            dict_circles[i] = 0
        dict_circles[i] += 1

    return '\n'.join(dict_circles.keys())


if __name__ == '__main__':
    n = int(input())
    arr = [input() for _ in range(n)]
    print(circles(arr))
