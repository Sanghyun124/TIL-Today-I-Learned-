dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(start):
    count = 1
    queue = [start]
    home = 0
    max_home = 0

    visited = [[0 for _ in range(n)] for _ in range(n)]

    while queue and count <= n + 2:
        size = len(queue)
        for _ in range(size):
            i, j = queue.pop(0)
            visited[i][j] = 1
            if homes[i][j] == 1:
                home += 1

            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]

                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
        else:
            profit = m * home - (2 * count * (count - 1) + 1)
            if profit >= 0:
                max_home = home if max_home < home else max_home
            count += 1

    return max_home


T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    homes = [list(map(int, input().split())) for _ in range(n)]

    max_house = 0

    for x in range(n):
        for y in range(n):
            house = bfs((x, y))
            max_house = house if max_house < house else max_house

    print(f'#{t + 1} {max_house}')
