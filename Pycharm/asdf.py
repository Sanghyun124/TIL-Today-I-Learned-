def check(ary):
    global n
    global x
    temp_ary=ary[:]
    for i in range(n - 1):
        if ary[i] > ary[i + 1]:
            if abs(ary[i] - ary[i + 1]) != 1:
                break
            for a in range(x - 1):
                if i + 1 + a + 1 >= n or temp_ary[i + 1 + a] != temp_ary[i + 1 + a + 1]:
                    break
            else:
                for a in range(x):
                    temp_ary[i + a + 1] = ary[i]
                continue
            return 0
        elif ary[i] < ary[i + 1]:
            if abs(ary[i] - ary[i + 1]) != 1:
                break
            for a in range(x - 1):
                if i - 1 - a < 0 or temp_ary[i - a] != temp_ary[i - 1 - a]:
                    break
            else:
                continue
            return 0
    else:
        print('count')
        return 1


for t in range(int(input())):
    n, x = map(int, input().split())
    ary = [list(map(int, input().split())) for _ in range(n)]
    trial = 0
    count = 0

    for i in range(n):
        trial+=1
        print(trial)
        new_ary = ary[i]
        if check(new_ary) == 1:
            count += 1

    for j in range(n):
        trial += 1
        print(trial)
        new_ary = [ary[i][j] for i in range(n)]
        if check(new_ary) == 1:
            count += 1
    print(f'#{t + 1} {count}')
