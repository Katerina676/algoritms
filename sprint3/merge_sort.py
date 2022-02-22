def merge(arr, lf, mid, rg):
    first = arr[lf:mid]
    second = arr[mid:rg]

    l, r, k = 0, 0, lf
    while l+lf < mid and r+mid < rg:
        if first[l] <= second[r]:
            arr[k] = first[l]
            l += 1
        else:
            arr[k] = second[r]
            r += 1
        k += 1

    while l < len(first):
        arr[k] = first[l]
        l += 1
        k += 1
    while r < len(second):
        arr[k] = second[r]
        r += 1
        k += 1

    return arr


def merge_sort(arr, lf, rg):
    if (rg - lf) == 1:
        return arr
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


print(test())
