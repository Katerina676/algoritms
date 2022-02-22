def team_count(team1, team2):
    count = {}
    long = 0
    length = 0
    if team1 == team2:
        return len(team1)
    for i, k in enumerate(team1):
        if k not in count:
            count[k] = [i]
        else:
            count[k].append(i)
    for i, k in enumerate(team2):
        if k not in count:
            continue
        if len(team2) - i <= long:
            break
        for idx in count.get(k):
            if len(team1) - idx <= long:
                break
            x = i
            y = idx
            while x < len(team2) and y < len(team1) and team1[y] == team2[x]:
                length += 1
                x += 1
                y += 1
            long = long if long > length else length
            length = 0
    return long


if __name__ == '__main__':
    n = int(input())
    team1 = input().split()
    n1 = int(input())
    team2 = input().split()
    if n >= n1:
        print(team_count(team1, team2))
    elif n <= n1:
        print(team_count(team2, team1))
