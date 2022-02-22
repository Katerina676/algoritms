# 63940152
import collections


def game_button(click):
    score = 0
    keys = collections.defaultdict(int)
    for i in range(4):
        nums = input()
        for k in nums:
            if k != '.':
                keys[k] += 1

    for i in keys:
        if keys[i] <= click * 2:
            score += 1
    return score


def main():
    click = int(input())
    print(game_button(click))


if __name__ == '__main__':
    main()