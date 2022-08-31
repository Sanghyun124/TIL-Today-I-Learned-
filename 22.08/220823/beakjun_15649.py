def back():
    global visited

    if sum(visited) == m:
        for a in range(n):
            if visited[a] == 1:
                print(ary[a], end=' ')
        print()
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            back()
            visited[i] = 0


n, m = map(int, input().split())
visited = [0] * n
ary = [i for i in range(1, n + 1)]
back()
