def main():
    s = input().strip()
    n = int(input().strip())
    result = [(0, '')] * n
    for i in range(n):
        sub, pos = input().strip().split()
        result[i] = (int(pos), sub)

    new_str = ''
    offset = 0
    for pos, sub in sorted(result):
        new_str += s[offset:pos] + sub
        offset = pos

    new_str += s[offset:]
    print(new_str)


if __name__ == '__main__':
    main()
