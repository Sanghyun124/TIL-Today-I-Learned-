def counting(ary):
    num = 0
    for a in ary:
        if a == 1:
            num += 1
    return num


t = int(input())
for test in range(t):
    k, n, m = map(int, input().split())  # k: 이동 정류장수, n:종점, m:충전기 개수
    charger = list(map(int, input().split()))
    bus_stop = []
    for i in range(n + 1):
        if i in charger:
            bus_stop.append(1)
        else:
            bus_stop.append(0)
    print(bus_stop)
    move = k
    count = 0
    for bus in range(n + 1):
        now = bus_stop[bus:bus + move + 1]
        if counting(now) == 1 and bus_stop[bus] == 1:
            move = k
            count += 1
        elif counting(now) == 0:
            count = 0
            break

        if bus + move >= n:
            break
        else:
            move -= 1

    print(f'#{test + 1} {count}')
