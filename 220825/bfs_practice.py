def bfs(ary, n, start):
    visited = [0] * (n + 1)

    front = 0
    rear = 0

    queue = [0] * (n + 1)

    visited[start] = 1
    count = 0
    rear += 1
    queue[rear] = start
    size = 1

    while rear != front:

        for _ in range(size):
            front = (front + 1) % len(queue)
            a = queue[front]
            size -= 1

            if a == g:
                return count

            for x in ary[a]:
                if visited[x] != 1:
                    visited[x] = 1
                    rear = (rear + 1) % len(queue)
                    queue[rear] = x
                    size += 1

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
    print(f'#{t + 1} {bfs(ary, v, s)}')
