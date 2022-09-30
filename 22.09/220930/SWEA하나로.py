import math


def distance(n1, n2):
    x1, y1 = island[n1]
    x2, y2 = island[n2]

    d = math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))

    return d


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for t in range(T):
    n = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    e = float(input())
    island = [(island_x[i], island_y[i]) for i in range(n)]
    p = [i for i in range(n)]
    count = 0  # 선택한 edge수
    total = 0

    ary = []
    for i in range(n):
        for j in range(i + 1, n):
            ary.append((distance(i, j), i, j))

    ary.sort()
    for w, x, y in ary:
        if find_set(x) != find_set(y):
            count += 1
            union(x, y)
            total += e*(w**2)
            if count == n - 1:
                break

    print(f'#{t+1} {round(total)}')