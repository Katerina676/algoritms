def length_word(words):
    count = 0
    word = ''
    for i, k in enumerate(words):
        if len(words[i]) > count:
            count = len(words[i])
            word = words[i]
        i += 1
    return f'{word}\n{count}'





n = int(input())
words = list(map(str, input().split()))
print(length_word(words))