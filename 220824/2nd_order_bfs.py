di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(si, sj, n):  # g: 그래프, v: 시작지점, n: 정점의 개수
    visited = [[0 for _ in range(n)] for _ in range(n)]

    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1
    day = 0

    while queue:
        # 내가 현재 위치에서 방문을 몇번 할건지 구하자.
        # 방문할 위치는 큐에 들어있고, 그 위치의 개수(큐의크기)를 구하면 된다.
        size = len(queue)

        for _ in range(size):
            # 현재 방문 위치 꺼내기
            i, j = queue.pop(0)

            print(f'{day}일차...')
            print('====================')
            for k in range(n):
                print(visited[k])
            print('====================')

            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
        day += 1


bfs(5, 5, 10)
