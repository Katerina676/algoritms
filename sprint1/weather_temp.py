def weather_random(days, temperatures):
    a = 0
    for i in range(days):
        today = temperatures[i]
        if i == 0:
            yesterday = today - 1
        else:
            yesterday = temperatures[i - 1]
        if i == (days - 1):
            tomorrow = today - 1
        else:
            tomorrow = temperatures[i + 1]
        if yesterday < today and today > tomorrow:
            a += 1
    return a




days = int(input())
temperatures = list(map(int, input().strip().split()))

print(weather_random(days, temperatures))
