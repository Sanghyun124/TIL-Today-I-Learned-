def check()



T=int(input())
for t in range(T):
    ary=list(map(int, input().split()))
    n=ary[0]
    ary=ary[1:]+[0]
    moved=0
    count=0



    print(f'#{t+1} {count}')