T = int(input())


def make_set(x):
    global p
    global rank
    p[x] = x
    rank[x] = 0


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


for t in range(T):
    n, m = map(int, input().split())
    ary = list(map(int, input().split()))
    n_ary = []
    for i in range(0, len(ary), 2):
        n_ary.append((ary[i], ary[i + 1]))
    p = [0] * (n + 1)
    rank = [0] * (n + 1)
    for x, y in n_ary:
        if p[x] == 0:
            make_set(x)
        if p[y] == 0:
            make_set(y)
        union(x, y)

    for i in range(1, n + 1):
        if p[i] == 0:
            p[i] = i
        else:
            find_set(i)
    p.pop(0)
    n_p = set(p)
    # print(p)
    # print(rank)
    print(f'#{t + 1} {len(n_p)}')
