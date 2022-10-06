T = int(input())

for test in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(n - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    print(f'#{test + 1} {num_list[n - 1] - num_list[0]}')