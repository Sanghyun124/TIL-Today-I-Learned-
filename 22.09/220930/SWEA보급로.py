from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def dijkstra(x, ary):
    D = [10000000] * (v)
    D[x] = 0
    q = deque([x])

    while q:
        node = q.popleft()

        for next, w in ary[node]:
            if D[node] + w < D[next]:
                D[next] = D[node] + w
                q.append(next)
    return D


T = int(input())
for t in range(T):
    n = int(input())
    ary = [list(map(int, list(input()))) for _ in range(n)]
    print(ary)
    v = n ** 2
    adj = [[] for _ in range(v)]
    for i in range(n):
        for j in range(n):
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < n and 0 <= nj < n:
                    adj[n * i + j].append((n * ni + nj, ary[ni][nj]))
    min_num = 10000000000000
    num = dijkstra(0, adj)
    print(f'#{t + 1} {num[-1]}')
