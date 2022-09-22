T = int(input())


def perm(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n - 1):
                result.append([arr[i]] + p)

    return result


for t in range(T):
    N = int(input())
    ary = [list(map(int, input().split())) for _ in range(N)]

    min_num = 1000000000000
    check_area = [i for i in range(2, N + 1)]
    possible_case = perm(check_area, N-1)
    print(possible_case)

    for case in possible_case:
        case.append(1)
        case.insert(0,1)
        total=0
        for x in range(N):
            total+=ary[case[x]-1][case[x+1]-1]
            if total>min_num:
                break
        min_num=total if min_num>total else min_num

    print(f'#{t+1} {min_num}')
    possible_case=[]