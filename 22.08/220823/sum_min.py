def backtracking(r, sum):
    global min_num
    global visited
    if r == n:
        min_num = sum if min_num > sum else min_num
    elif sum>=min_num:
        return

    for c in range(n):
        if visited[c] == 0:
            visited[c] = 1
            backtracking(r + 1, sum + ary[r][c])
            visited[c] = 0


T = int(input())
for t in range(T):
    n = int(input())
    ary = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_num = 999
    backtracking(0, 0, visited)
    print(f'#{t + 1} {min_num}')
