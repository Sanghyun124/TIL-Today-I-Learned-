dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, -1, 0, 1, -1]

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    ary = [[0 for _ in range(n)] for _ in range(n)]
    ary[n // 2 - 1][n // 2 - 1] = 2
    ary[n // 2 - 1][n // 2] = 1
    ary[n // 2][n // 2 - 1] = 1
    ary[n // 2][n // 2] = 2
    for _ in range(m):
        j, i, a = map(int, input().split())
        ary[i - 1][j - 1] = a

        for d in range(8):
            count = 0
            ni = i - 1 + dx[d]
            nj = j - 1 + dy[d]

            while 0 <= ni < n and 0 <= nj < n and ary[ni][nj] != 0:
                if ary[ni][nj] == a:
                    for p in range(1, count + 1):
                        ary[i - 1 + p * dx[d]][j - 1 + p * dy[d]] = a
                    break
                else:
                    ni = ni + dx[d]
                    nj = nj + dy[d]
                    count += 1

    b_count = 0
    w_count = 0
    for x in range(n):
        for y in range(n):
            if ary[x][y] == 1:
                b_count += 1
            elif ary[x][y] == 2:
                w_count += 1
    print(f'#{t + 1} {b_count} {w_count}')