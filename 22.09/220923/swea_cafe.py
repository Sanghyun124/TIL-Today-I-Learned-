dj = [1, -1, -1, 1]
di = [1, 1, -1, -1]

def search(i,j, route,dir):
    route.append(i,j)
    if dir==1:
        



T = int(input())
for t in range(T):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]

    possible_route = []

    for i in range(1, n - 1):
        for j in range(n - 2):
            for dx in range(1,n-i):
                for dy in range(1,n-1-dx):
                    temp=[(i,j)]
                    temp.append(())


