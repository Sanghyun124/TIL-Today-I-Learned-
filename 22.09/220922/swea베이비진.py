def check_run(p):
    if len(p)<3:
        return 0
    else:
        p=sorted(list(set(p)))
        for a in range(len(p) - 2):
            if p[a + 1] - p[a] == 1 and p[a + 2] - p[a + 1] == 1:
                return 1
        else:
            return 0


def check_triplet(p):
    count = [0] * 10
    for num in p:
        count[num] += 1

    if 3 in count:
        return 1
    else:
        return 0


T = int(input())
for t in range(T):
    print(f'#{t + 1} ', end='')
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    for i in range(12):
        if i % 2:
            p2.append(cards[i])
            p2.sort()
            if check_run(p2) or check_triplet(p2):
                print(2)
                break
        else:
            p1.append(cards[i])
            p1.sort()
            if check_run(p1) or check_triplet(p1):
                print(1)
                break
    else:
        print(0)
