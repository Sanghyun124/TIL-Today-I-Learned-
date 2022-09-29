from collections import deque


def dijkstra(s, adj):
    D = [1000000000] * (n+1)
    D[s] = 0
    q = deque([s])

    while q:
        now = q.popleft()
        for next, w in adj[now]:
            if D[now] + w < D[next]:
                D[next] = D[now] + w
                q.append(next)
    return D


T = int(input())
for t in range(T):
    n, e = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(e):
        x, y, w = map(int, input().split())
        adj[x].append((y, w))

    distance = dijkstra(0, adj)
    print(f'#{t + 1} {distance[-1]}')
