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
        p[y] = x
        if rank[x] == rank[y]:
            rank[y] += 1

for t in range(T):
    n,m=map(int,input().split())
    p=[i for i in range(n+1)]
    rank=[0]*(n+1)
    for _ in range(m):
        p1,p2=map(int,input().split())
        union(p1,p2)
    for x in range(n+1):
        find_set(x)
    p.pop(0)
    s_p=set(p)
    print(f'#{t+1} {len(s_p)}')