def hash(a, m, s):
    x = 0
    for i in s:
        x = (x * a + ord(i)) % m
    return x


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input().strip()
    print(hash(a, m, s))
