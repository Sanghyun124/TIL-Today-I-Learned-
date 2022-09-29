T = int(input())


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)



for t in range(T):
    v, e = map(int, input().split())
    ary = []
    for _ in range(e):
        x, y, num = map(int, input().split())
        ary.append((x, y, num))
    ary.sort(key=lambda x: x[2])
    p = [i for i in range(v+1)]
    n=v+1
    count=0#선택한 edge수
    total=0

    for x,y,w in ary:
        if find_set(x)!=find_set(y):
            count+=1
            union(x,y)
            total+=w
            if count==n-1:
                break
    print(f"#{t+1} {total}")
