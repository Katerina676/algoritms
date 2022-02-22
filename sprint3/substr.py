def substr(s, t):
    x = 0
    if s == '':
        return True
    for i in range(len(t)):
        if t[i] == s[x]:
            x += 1
            if len(s) == x:
                return True
    return False


if __name__ == '__main__':
    s = input()
    t = input()
    print(substr(s, t))
