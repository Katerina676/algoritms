def substr(s):
    hash = {}
    next = 0
    result = []
    for i in s:
        if i not in hash:
            hash[i] = next
            next += 1
        result.append(hash[i])
    return result


def gt(s, s1):
    x = substr(s)
    y = substr(s1)
    res = 'YES' if x == y else 'NO'
    return res


if __name__ == '__main__':
    s = input()
    s1 = input()
    print(gt(s, s1))
