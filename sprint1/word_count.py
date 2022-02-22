def length_word(short, long):
    dict = {}
    dict1 = {}
    for i in short:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    for i in long:
        if i not in dict1.keys():
            dict1[i] = 1
        else:
            dict1[i] += 1
    for key, value in dict1.items():
        if key in dict:
            if value > dict[key]:
                return key
        elif key not in dict:
            return key










short = input().strip()
long = input().strip()
print(length_word(short, long))