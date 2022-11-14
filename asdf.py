from collections import deque

di=[1,0,-1,0]
dj=[0,1,0,-1]

def bfs(start):
    global visited
    q=deque([start])

    while q:
        i,j=q.popleft()

        for d in range(4):
            ni=i+di[d]
            nj=j+dj[d]

            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0 and ary[ni][nj]==1:
                visited[ni][nj]=1
                q.append((ni,nj))
                print(ni,nj)
                counts[-1]+=1


n=int(input())
ary=[list(map(int,list(input()))) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
counts=[]
for a in range(n):
    for b in range(n):
        # print(a,b)
        if ary[a][b]==1 and visited[a][b]==0:
            counts.append(1)
            visited[a][b]=1
            bfs((a,b))

counts.sort()
print(len(counts))
for x in counts:
    print(x)