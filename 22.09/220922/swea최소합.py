T=int(input())
for t in range(T):
    n=int(input())
    ary=[list(map(int,input().split())) for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if a==0and b==0:
                continue
            elif a==0:
                ary[a][b]+=ary[a][b-1]
            elif b==0:
                ary[a][b] += ary[a-1][b]
            else:
                ary[a][b]+=ary[a-1][b] if ary[a-1][b]<ary[a][b-1] else ary[a][b-1]

    print(f'#{t+1} {ary[-1][-1]}')
