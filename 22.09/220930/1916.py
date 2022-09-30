from collections import deque


def dijkstra(x, ary):
    D = [1000000000] * (n + 1)
    D[x] = 0
    q = deque([x])

    while q:
        node = q.popleft()

        for next, w in ary[node]:
            if D[node] + w < D[next]:
                D[next] = D[node] + w
                q.append(next)
    return D


n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, s = map(int, input().split())
    adj[a].append((b, s))
start, end = map(int, input().split())

ary = dijkstra(start, adj)

print(ary[end])
