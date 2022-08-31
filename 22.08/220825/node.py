def bfs(ary, s, v):
    queue = []
    visited = [0] * (v + 1)

    queue.append(s)
    visited[s] = 1
    count = 0

    while queue:

        size = len(queue)

        for _ in range(size):

            a = queue.pop(0)
            if a == g:
                return count

            for i in ary[a]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
        count += 1
    else:
        return 0


T = int(input())
for t in range(T):
    v, e = map(int, input().split())
    ary = [[] for _ in range(v + 1)]
    for _ in range(e):
        p, q = map(int, input().split())
        ary[p].append(q)
        ary[q].append(p)
    s, g = map(int, input().split())
    print(f'#{t + 1} {bfs(ary, s, v)}')
