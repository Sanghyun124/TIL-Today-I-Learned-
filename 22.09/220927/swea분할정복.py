def bin_search(l, r, select):
    global result
    # print(l,r,select)
    m = (l + r) // 2
    result.append(a_ary[m])
    # print(result)
    if r-l<1:
        return
    if select == 0:
        bin_search(l, m - 1, 'l')
        bin_search(m + 1, r, 'r')
    else:
        if select == 'r' and m-1>=l:
            bin_search(l, m - 1, 'l')
        elif select == 'l':
            bin_search(m + 1, r, 'r')


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    a_ary = sorted(list(map(int, input().split())))
    b_ary = list(map(int, input().split()))
    result = []
    count = 0

    bin_search(0, N - 1, 0)
    for num in b_ary:
        if num in result:
            count += 1

    print(f'#{t + 1} {count}')
