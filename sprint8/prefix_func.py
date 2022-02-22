def prefix_func(s):
    prefix = [0] * len(s)
    j = 0
    i = 1

    while i < len(s):
        if s[j] != s[i]:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1
        else:
            prefix[i] = j + 1
            i += 1
            j += 1

    return prefix


def main():
    s = input().strip()

    print(' '.join(map(str, prefix_func(s))))


if __name__ == '__main__':
    main()
