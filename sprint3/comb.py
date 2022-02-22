def get_comb(prefix, line, res):
    button = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if 0 == len(line):
        res.append(prefix)
    else:
        for i in button.get(line[0]):
            get_comb(prefix+i, line[1:], res)


if __name__ == '__main__':
    line = input()
    res = []
    get_comb('', line, res)
    print(*res)
