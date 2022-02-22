def matrixes(lines, a, b, n, m):
    count = []
    if n == 1 and m == 1:
        return ''
    elif n == 1:
        if b == 0:
            count.append(lines[a][b+1])
        elif b == m - 1:
            count.append(lines[a][b-1])
        else:
            count.append(lines[a][b+1])
            count.append(lines[a][b-1])

    elif m == 1:
        if a == 0:
            count.append(lines[a+1][b])
        elif b == n - 1:
            count.append(lines[a-1][b])
        else:
            count.append(lines[a-1][b])
            count.append(lines[a+1][b])
    else:
        if a == 0:
            if b == 0:
                count.append(lines[a+1][b])
                count.append(lines[a][b+1])
            elif lines[a][-1] == lines[a][b]:
                count.append(lines[a+1][b])
                count.append(lines[a][b-1])
            else:
                count.append(lines[a+1][b])
                count.append(lines[a][b-1])
                count.append(lines[a][b+1])
        elif lines[-1][b] == lines[a][b]:
            if b == 0:
                count.append(lines[a - 1][b])
                count.append(lines[a][b+1])
            elif lines[a][-1] == lines[a][b]:
                count.append(lines[a-1][b])
                count.append(lines[a][b-1])
            else:
                count.append(lines[a-1][b])
                count.append(lines[a][b-1])
                count.append(lines[a][b+1])
        elif a != 0 and lines[-1][b] != lines[a][b]:
            if b == 0:
                count.append(lines[a+1][b])
                count.append(lines[a-1][b])
                count.append(lines[a][b+1])
            elif lines[a][-1] == lines[a][b]:
                count.append(lines[a-1][b])
                count.append(lines[a+1][b])
                count.append(lines[a][b-1])
            else:
                count.append(lines[a+1][b])
                count.append(lines[a-1][b])
                count.append(lines[a][b-1])
                count.append(lines[a][b+1])






    return sorted(count)



n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().strip().split())))
a = int(input())
b = int(input())
print(*matrixes(matrix, a, b, n, m))