def foo(a, x, b, c):
    y = a * x * x + b * x + c
    return y

a, x, b, c = map(int, input().split())
print(foo(a, x, b, c))