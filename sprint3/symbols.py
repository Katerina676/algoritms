def gen_binary(n, prefix, left, right):
    if left == n and right == n:
        return print(prefix)
    else:
        if left < n:
            gen_binary(n, prefix + '(', left+1, right)
        if right < left:
            gen_binary(n, prefix + ')', left, right+1)


if __name__ == '__main__':
    gen_binary(int(input()), '', 0, 0)
