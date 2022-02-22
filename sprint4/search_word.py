# --- ПРИНЦИП РАБОТЫ ---
# Для хранения слов используем словарь.Будем искать уникальные слова из запроса в словаре и сохранять в новом словаре
# сколько раз они встретились и в каком именно документе.
# --- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ ---
# Каждое уникальное слово мы проверяем в словаре, есть ли оно, если есть ищем в каких именно докумнтах оно встречается
# и сколько раз.Сортируем и выводим 5 первых релевантных результатов.
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
# Сложность алгоритма О(n),так как мы проходим по всем словам в поиске,где n зависит от количества и размера
# слов-документов.
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
# Алгоритм будет занимать О(n) памяти так как хранятся слова и их индексы в словаре.
# id 64523433
import collections


def dict_documents(word):
    docs = {}
    for i in range(len(word)):
        for j in word[i].split():
            val = docs.get(j, {})
            val[i] = val.get(i, 0) + 1
            docs[j] = val
    return docs


def search_word(words, request):
    # word = {}
    word = collections.defaultdict(int)
    for i in set(request.split()):
        if i in words.keys():
            for index, count in words[i].items():
                word[index] = word.get(index, 0) + count
    result = sorted(word.items(), reverse=True, key=lambda x: (x[1], -x[0]))
    print(*map(lambda x: x[0] + 1, result[:5]))


if __name__ == '__main__':
    n = int(input())
    word = [input() for _ in range(n)]
    words = dict_documents(word)
    m = int(input())
    req = [input() for _ in range(m)]
    for i in req:
        search_word(words, i)
