from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(start):
    count = 0
    queue = deque()
    queue.append(start)

    visited = [[0 for _ in range(n)] for _ in range(n)]

    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()
            visited[i][j] = 1

            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]

                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and ary[ni][nj] - ary[i][j] == 1:
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
                    break
        else:
            count += 1

    return count


T = int(input())
for t in range(T):
    n = int(input())
    ary = [list(map(int, input().split())) for _ in range(n)]
    min_num = 1000000
    max_count = 0

    for x in range(n):
        for y in range(n):
            temp = bfs((x, y))
            print((x, y))
            if max_count <= temp:
                if max_count != temp:
                    min_num = ary[x][y]
                max_count = temp
                if min_num > ary[x][y]:
                    min_num = ary[x][y]

    print(f'#{t + 1} {min_num} {max_count}')
