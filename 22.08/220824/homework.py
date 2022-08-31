for t in range(1,11):
    n=int(input())
    queue = list(map(int, input().split()))

    while True:
        for i in range(1, 6):
            a = queue.pop(0) - i
            if a <= 0:
                a = 0
                queue.append(a)
                break
            queue.append(a)
        else:
            continue
        break
    print(f'#{t} ', end='')
    print(*queue)