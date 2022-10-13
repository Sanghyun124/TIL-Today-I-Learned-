def p(stg,temp):
    if stg>m:
        print(*temp)
        return
    else:
        for i in range(n):
            if len(temp)==0:
                temp.append(ary[i])
                p(stg+1,temp)
                temp.pop()
            elif temp[-1]<=ary[i]:
                temp.append(ary[i])
                p(stg+1,temp)
                temp.pop()



n,m=map(int,input().split())
ary=sorted(list(map(int,input().split())))
p(1,[])
