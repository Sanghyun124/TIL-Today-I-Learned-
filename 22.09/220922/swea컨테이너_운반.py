T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())))
    t = sorted(list(map(int, input().split())), reverse=True)
    # print(w)
    # print(t)
    total = 0
    for truck in range(m):
        while w:
            now_w=w.pop()
            if t[truck]>=now_w:
                t[truck]=now_w
                break
        else:
            t[truck]=0



    print(f'#{tc + 1} {sum(t)}')
