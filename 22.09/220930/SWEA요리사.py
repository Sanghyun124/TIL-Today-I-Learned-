T = int(input())
for t in range(T):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    ary = [i for i in range(1, n + 1)]
    n_ary = []
    for x in range(1 << n):
        temp = []
        for y in range(n):
            if x & (1 << y):
                temp.append(ary[y])
        if len(temp) == n // 2:
            n_ary.append(temp)

    pair = []
    for i in range(len(n_ary) // 2):
        pair.append((n_ary[i], n_ary[len(n_ary) - 1 - i]))

    min_num = 10000000000000000
    for A, B in pair:
        temp_a = 0
        temp_b = 0
        for i in A:
            for j in A:
                temp_a += s[i-1][j-1]

        for i in B:
            for j in B:
                temp_b += s[i-1][j-1]

        min_num = abs(temp_b - temp_a) if min_num > abs(temp_b - temp_a) else min_num

    print(f'#{t + 1} {min_num}')
