def list_form(lists, k):
    new = [i for i in lists if i != ' ']
    new_lists = ''.join(new)
    summa = int(new_lists) + k
    return [i for i in str(summa)]



n = int(input())
lists = list(map(str, input().split()))
k = int(input())

print(*list_form(lists, k))