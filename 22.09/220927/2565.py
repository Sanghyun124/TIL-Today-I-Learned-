n=int(input())
ary=[]
for _ in range(n):
    ary.append(list(map(int,input().split())))
ary.sort(key=lambda x : x[0])
count=[]
stack=[0]
while stack:
    start=stack.pop(0)
    temp=[]
    for x in range(start,n):
        if not temp:
            temp.append(ary[x][1])
            continue
        if temp[-1]<ary[x][1]:
            temp.append(ary[x][1])
        else:
            stack.append(x)
        print(temp)
    count.append(len(temp))

max_count=max(count)


print(n-max_count)