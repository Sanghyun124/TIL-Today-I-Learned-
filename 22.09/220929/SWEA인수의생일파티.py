from collections import deque

def dijkstra(x, ary):
    D=[inf]*(n+1)
    D[x]=0
    q=deque([x])

    while q:
        node=q.popleft()
        for next,w in ary[node]:
            if D[node]+w<D[next]:
                D[next]=D[node]+w
                q.append(next)
    return D

T = int(input())
for t in range(T):
    n, m, x = map(int, input().split())
    inf = 10000000
    adj_go = [[] for _ in range(n + 1)]
    adj_come = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_go[u].append((v, w))  # 집에 돌아올 때
        adj_come[v].append((u, w))  # 파티 갈 때

    go_d = dijkstra(x, adj_go)
    come_d = dijkstra(x, adj_come)
    max_num = 0
    for i in range(1,n+1):
        distance=go_d[i]+come_d[i]
        if distance>max_num:
            max_num=distance
    print(f'#{t+1} {max_num}')
