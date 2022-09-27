def quick(ary, l, r):
    if l < r:
        s = partition(ary, l, r)
        quick(ary, l, s - 1)
        quick(ary, s + 1, r)

    return ary


def partition(ary, l, r):
    p = ary[l]
    i, j = l, r
    while i <= j:
        while i <= j and ary[i] <= p:
            i += 1
        while i <= j and ary[j] >= p:
            j -= 1
        if i < j:
            ary[i], ary[j] = ary[j], ary[i]

    ary[l], ary[j] = ary[j], ary[l]
    return j


T = int(input())
for t in range(T):
    n = int(input())
    ary = list(map(int, input().split()))
    result=quick(ary,0,n-1)

    print(f'#{t+1} {result[n//2]}')
