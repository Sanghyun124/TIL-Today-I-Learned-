T = int(input())


# cnt:카드를 교환한 횟수
def card_swap(cnt):
    global max_val

    # 중단 조건
    # 교환 횟수를 다 썻으면 그때 최대 상금을 구하면 된다.
    if cnt == N:
        num = int(''.join(S))
        max_val = max(max_val, num)
        return

    # 부분 문제
    # 교환 횟수가 남아있으면 카드를 바꾸기
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            # i위치의 카드와 j위치의 카드를 교환
            S[i], S[j] = S[j], S[i]
            # 교환한 상태로 다음 교환으로 넘어가기
            card_swap(cnt + 1)
            # 계산 했으면 교환 전의 상태로 되돌린다
            S[i], S[j] = S[j], S[i]


for t in range(T):
    S, N = input().split()
    S = list(S)
    N = int(N)

    # 똑같은 자리에서 교환 중복을 허용한다고 했지만
    # 결국 우리가 해당 자리수로 만들 수 있는 숫자는
    # 해당 자리수만큼 교환을 실행한 결과와 같을것이다:
    # 주어진 교환 횟수가 카드의 수 보다 커지면
    # 의미가 없어진다. 그 경우에는 교환 횟수를 카드의 수로 제한

    if N > len(S):
        N = len(S)

    # 카드로 만들 수 있는 최대값
    max_val=0

    #교환횟수 0번부터 바꿔라
    card_swap(0)

    print(f'#{t+1} {max_val}')