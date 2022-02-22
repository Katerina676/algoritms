def main():
    a = input()
    b = input()

    list_a = [i for i in a if ord(i) % 2 == 0]
    list_b = [i for i in b if ord(i) % 2 == 0]

    if list_a == list_b:
        print(0)
    elif list_a > list_b:
        print(1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
