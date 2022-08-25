di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(ary, n, start):
    i, j = start

    visited = [[0 for _ in range(n)] for _ in range(n)]

    queue = []
    visited[i][j] = 1
    queue.append((i, j))
    count = 0

    while queue:
        size = len(queue)
        for _ in range(size):

            i, j = queue.pop(0)

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and ary[ni][nj] != 1:
                    if ary[ni][nj] == 3:
                        return count

                    visited[ni][nj] = 1
                    queue.append((ni, nj))
        count += 1
    else:
        return 0


T = int(input())
for t in range(T):
    n=int(input())
    ary = [list(map(int, list(input()))) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if ary[i][j]==2:
                si=i
                sj=j

    print(f'#{t+1} {bfs(ary,n,(si,sj))}')


