from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dijkstra(s,adj):
    D=[10000000000]*(v)
    D[s]=0
    q=deque([s])

    while q:
        node=q.popleft()
        for next,w in adj[node]:
            if D[node]+w<D[next]:
                D[next]=D[node] + w
                q.append(next)
    return D

T = int(input())
for t in range(T):
    n = int(input())
    ary = [list(map(int, input().split())) for _ in range(n)]
    v = n ** 2
    adj = [[] for _ in range(v)]
    for i in range(n):
        for j in range(n):
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < n and 0 <= nj < n:
                    adj[n * i + j].append((n * ni + nj, 1 + ((ary[ni][nj]-ary[i][j]) if ary[ni][nj] > ary[i][j] else 0)))
    min_num=dijkstra(0,adj)[-1]

    print(f'#{t+1} {min_num}')