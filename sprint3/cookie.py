def cookie(greedy, sizes, cookies):
    happy = 0
    a = 0
    for i in greedy:
        for j in range(a, cookies):
            if sizes[j] > i:
                a = j+1
                happy += 1
                break

    return happy


if __name__ == '__main__':
    n = int(input())
    greedy = [int(i) for i in input().split()]
    cookies = int(input())
    sizes = [int(i) for i in input().split()]
    greedy.sort()
    sizes.sort()
    print(cookie(greedy, sizes, cookies))
