def bubble_sort(length, arr):
    for i in range(length):
        flag = False
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag == False:
            if i == 0:
                print(*arr)
            break
        print(*arr)


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    bubble_sort(n, arr)