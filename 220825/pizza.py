T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    ary = [0] + list(map(int, input().split()))
    num_ary = list(range(1, m + 1))
    queue = []
    i = 1
    while i <= m + 1:
        if len(queue) < n:
            queue.append(i)
            i += 1
            continue
        while True:
            if len(queue) == 1:
                break
            index = queue.pop(0)
            check = ary[index]
            check = check // 2
            if check == 0:
                if i!=m+1:
                    ary[index] = check
                    break
                else:
                    continue
            else:
                ary[index] = check
                queue.append(index)
    print(f'#{t + 1} {queue.pop(0)}')
