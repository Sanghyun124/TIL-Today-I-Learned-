def check(row, col, visited, total):
    global min_num
    n_total=total+ary[row][col]
    if n_total>min_num:
        return
    visited[col] = 1
    print(visited)
    print(row,col,n_total)
    if sum(visited)==n:
        min_num = n_total if n_total < min_num else min_num
        return
    for x in range(n):
        if not visited[x]:
            check(row + 1, x, visited, n_total)
            visited[x]=0


T = int(input())
for t in range(T):
    n = int(input())
    ary = [list(map(int, input().split())) for _ in range(n)]
    min_num = 99 * 5 + 1
    for col in range(n):
        check(0, col, [0] * n, 0)

    print(f'#{t + 1} {min_num}')
