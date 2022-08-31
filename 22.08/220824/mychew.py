n = int(input())
queue = []
for _ in range(n):
    s = list(input().split())
    if s[0] == 'push':
        queue.append(s[1])
    elif s[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(queue))

    elif s[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
