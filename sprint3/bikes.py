def bikes(cost, days, left, right):
    lens = right - left + 1
    if lens < 1:
        return -1
    mid = (left + right) // 2
    if lens == 1 and cost <= days[mid]:
        return mid + 1
    elif cost <= days[mid]:
        return bikes(cost, days, left, mid)
    else:
        return bikes(cost, days, mid+1, right)


if __name__ == '__main__':
    n = int(input())
    days = [int(i) for i in input().split()]
    cost = int(input())
    a = bikes(cost, days, 0, n-1)
    b = bikes(cost+cost, days, 0, n-1)
    print(a, b)
