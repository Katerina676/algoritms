def main():
    text = input()
    old = input()
    t = input()
    s = old + '#' + text
    dp = [0] * len(old)
    dp_prev = 0
    result = []

    for i in range(1, len(s)):
        k = dp_prev
        while (k > 0) and (s[k] != s[i]):
            k = dp[k - 1]
        if s[k] == s[i]:
            k += 1
        if i < len(old):
            dp[i] = k

        if i > len(old):
            result.append(s[i])

        dp_prev = k

        if k == len(old):
            for _ in range(len(old)):
                result.pop()

            for j in t:
                result.append(j)

    print(''.join(result))


if __name__ == '__main__':
    main()
