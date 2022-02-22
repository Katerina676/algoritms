# id 63704215

def step_to_zero(n, street):
    dist = [0] * n
    zero_position = [i for i, k in enumerate(street) if k == 0]

    for i in range(zero_position[0]):
        dist[i] = zero_position[0] - i

    for left, right in zip(zero_position[:-1], zero_position[1:]):
        for i in range(left + 1, right):
            dist[i] = min(i - left, right - i)

    for i in range(zero_position[-1] + 1, n):
        dist[i] = i - zero_position[-1]

    return dist


n = int(input())
street = list(map(int, input().split()))
print(*step_to_zero(n, street))
