T = int(input())

for t in range(T):
    n = int(input())
    schedule = [list(map(int, input().split())) for _ in range(n)]
    schedule.sort(key=lambda x: x[1],reverse=True)

    # print(schedule)

    end_time=schedule.pop()[1]

    max_cnt = 1

    while schedule:
        s,e=schedule.pop()
        if end_time<=s:
            end_time=e
            max_cnt+=1

    print(f'#{t + 1} {max_cnt}')
