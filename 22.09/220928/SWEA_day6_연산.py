from collections import deque

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    queue = deque([n])
    checked=[0]*1000001
    cnt = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            now = queue.popleft()
            if now == m:
                queue = []
                break
            else:
                if 1 <= now + 1 <= 1000000 and not checked[now + 1]:
                    queue.append(now + 1)
                    checked[now + 1]=1
                if 1 <= now * 2 <= 1000000 and not checked[now*2]:
                    queue.append(now * 2)
                    checked[now *2]=1
                if 1 <= now - 1 <= 1000000 and not checked[now - 1]:
                    queue.append(now - 1)
                    checked[now - 1]=1
                if 1 <= now - 10 <= 1000000 and not checked[now - 10]:
                    queue.append(now - 10)
                    checked[now - 10]=1
        else:
            cnt += 1

    print(f'#{t + 1} {cnt}')
