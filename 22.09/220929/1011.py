from collections import deque
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    cnt=1
    start=1
    for i in range(1,y-x+2):
        if not i%2:
            start+=1

    print(start)




