from collections import deque


def dijkstra(x, ary):
    D = [1000000] * (n + 1)
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

for _ in range(T):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append((a, s))


    ary = dijkstra(c, adj)
    count=0
    for i in range(len(ary)):
        if ary[i]==1000000:
            ary[i]=0
            count+=1
    count=n-count+1
    print(count,ary[-1])
