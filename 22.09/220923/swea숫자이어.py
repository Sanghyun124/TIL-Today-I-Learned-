from copy import deepcopy
from collections import deque
T = int(input())
for t in range(T):
    ary = [list(input().split()) for _ in range(4)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    possible_route = []

    for i in range(4):
        for j in range(4):
            queue = deque([[(i, j)]])

            while queue:
                check = queue.popleft()
                if len(check) == 7:
                    possible_route.append(check)
                    continue
                now = check[-1]

                for d in range(4):
                    ni = now[0] + di[d]
                    nj = now[1] + dj[d]

                    if 0 <= ni < 4 and 0 <= nj < 4:
                        temp=deepcopy(check)
                        temp.append((ni, nj))
                        queue.append(temp)


    for x in range(len(possible_route)):
        possible_route[x] = [ary[x][y] for x, y in possible_route[x]]
        possible_route[x] = ''.join(list(map(str, possible_route[x])))

    print(f'#{t+1} {len(set(possible_route))}')
