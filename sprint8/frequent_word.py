def main():
    n = int(input().strip())
    words = {}

    for _ in range(n):
        word = input()
        words[word] = words.get(word, 0) + 1
    return sorted(list(words.items()), key=lambda item: (-item[1], item[0]))[0][0]


if __name__ == '__main__':
    print(main())
