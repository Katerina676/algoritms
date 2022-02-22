def key(x, y):
    return int(x + y) > int(y + x)


def big_num(length, arr, key):
    for i in range(length):
        j = i
        item = arr[i]
        while j > 0 and key(item, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
            arr[j] = item
    return ''.join(arr)


if __name__ == '__main__':
    n = int(input())
    arr = [i for i in input().split()]
    print(big_num(n, arr, key=key))
