direction={
    'u':(-1,0),
    'd':(1,0),
    'l':(0,-1),
    'r':(1,0)
}

T = int(input())
for t in range(T):
    n = int(input())
    pinball = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if pinball[i][j]==0:
                start=(i,j)
            else:
                continue
            for dir in direction.keys():
                start+=dir

