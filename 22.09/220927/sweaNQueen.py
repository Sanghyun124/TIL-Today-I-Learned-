def check(i):
    global count
    if i == n:
        count += 1
    else:
        for j in range(n):
            if ary[j] == 0 and left[i + j] == 0 and right[i + n - 1 - j] == 0:
                ary[j] = 1
                left[i + j] = 1
                right[i + n - 1 - j] = 1
                print(ary)
                check(i + 1)
                ary[j] = 0
                left[i + j] = 0
                right[i + n - 1 - j] = 0


T = int(input())
for t in range(T):
    n = int(input())
    count = 0
    ary = [0] * n
    left = [0] * (2 * n - 1)
    right = [0] * (2 * n - 1)
    check(0)

    print(f'#{t + 1} {count}')
