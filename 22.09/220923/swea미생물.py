dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

T = int(input())
for t in range(T):
    n, m, k = map(int, input().split())
    ary = [[0] * n for _ in range(n)]
    for a in range(n):
        ary[a][0] = 'b'
        ary[0][a] = 'b'
        ary[a][n - 1] = 'b'
        ary[n - 1][a] = 'b'
    for _ in range(k):
        i, j, num, dir = map(int, input().split())
        ary[i][j] = [num, dir]

    for _ in range(m):
        temp_ary = [[[] for _ in range(n)] for _ in range(n)]
        print('---------------------------')
        for alpha in range(n):
            print(ary[alpha])
        for i in range(n):
            for j in range(n):
                if type(ary[i][j]) == list:
                    ni, nj = i + dy[ary[i][j][1]], j + dx[ary[i][j][1]]
                    if 0 <= ni < n and 0 <= nj < n:
                        print((i,j),(ni,nj))
                        if ary[ni][nj] == 'b':
                            ary[i][j][1] = ary[i][j][1] + 1 if ary[i][j][1] % 2 else ary[i][j][1] - 1
                            ary[i][j][0] = ary[i][j][0] // 2
                            temp_ary[ni][nj] = ary[i][j][:]
                        else:
                            temp_ary[ni][nj].append(ary[i][j][:])
                            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                                ary[i][j] = 'b'
                            else:
                                ary[i][j] = 0

        print('-------------temp--------------')
        for alpha in range(n):
            print(temp_ary[alpha])
        for i in range(0, n):
            for j in range(0, n):
                if len(temp_ary[i][j]) > 1:
                    temp_ary[i][j].sort(key=lambda x: x[0])
                    for x in range(len(temp_ary[i][j]) - 1):
                        temp_ary[i][j][x + 1][0] += temp_ary[i][j][x][0]
                    temp_ary[i][j] = temp_ary[i][j][-1]
                    ary[i][j] = temp_ary[i][j]
                elif len(temp_ary[i][j]) == 1:
                    temp_ary[i][j] = temp_ary[i][j][0]
                    ary[i][j] = temp_ary[i][j]
                else:
                    if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                        ary[i][j] = 'b'
                    else:
                        ary[i][j] = 0
    total = 0
    for i in range(n):
        for j in range(n):
            if type(ary[i][j]) == list:
                total += ary[i][j][0]
    print(f'#{t + 1} {total}')
