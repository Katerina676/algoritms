def substr_count(s):
    chars = {}
    long = 0
    curr = 0
    for i in range(len(s)):
        if s[i] in chars:
            if chars[s[i]] >= curr:
                curr = chars[s[i]] + 1
        curr_long = i - curr + 1
        long = long if long > curr_long else curr_long
        chars[s[i]] = i
    return long


if __name__ == '__main__':
    s = input()
    print(substr_count(s))
