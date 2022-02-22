def nums(a, b, c):
    if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0) or (a % 2 != 0 and b % 2 != 0 and c % 2 != 0):
        return 'WIN'
    return 'FAIL'

a, b, c = map(int, input().strip().split())
print(nums(a, b, c))