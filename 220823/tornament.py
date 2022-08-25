def game(a, b):
    x = ary[a]
    y = ary[b]
    if (x < y and (y - x) == 1) or (y == 1 and x == 3):
        return b
    elif a == b:
        return a
    else:
        return a


def partition(i, j):
    if i==j:
        return i
    else:
        left = partition(i, (i + j) // 2)
        right = partition((i + j) // 2 + 1, j)
        return game(left,right)



T = int(input())
for t in range(T):
    n = int(input())
    ary = list(map(int, input().split()))
    print(f'#{t+1} {partition(0,n-1)+1}')
