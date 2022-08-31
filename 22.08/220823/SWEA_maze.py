T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if maze[x][y] == 2:
                i_start = x
                j_start = y

    i = i_start
    j = j_start
    stack = []
    while True:
        # print(f'({i},{j})')
        # print(stack)
        visited[i][j] = 1
        for a in range(4):
            ni = i + di[a]
            nj = j + dj[a]

            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append((i, j))
                i, j = ni, nj
                break
        else:
            if len(stack) == 0:
                print(f'#{t} 0')
                break
            else:
                i, j = stack.pop()

        if maze[i][j] == 3:
            print(f'#{t} 1')
            break
