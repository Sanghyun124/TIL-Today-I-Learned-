v = int(input())
s = list(map(int, input().split()))
c = [[0 for _ in range(v + 1)], [0 for _ in range(v + 1)]]
for i in range(0, len(s), 2):
    if c[0][s[i]] != 0:
        c[1][s[i]] = s[i + 1]
    else:
        c[0][s[i]] = s[i + 1]

visited = [0] * (v + 1)

start = 1
stack = []

node = start
visited[node] = 1
stack.append(node)

while True:
    print(node, end=' ')
    check = node
    for i in range(2):
        node = c[i][node]
        if visited[check] == 0 and (c[0][check] != 0 or c[1][check] != 0):
            visited[node] = 1
            stack.append(node)
            break
    else:
        if stack:
            node = stack.pop()
        else:
            break
