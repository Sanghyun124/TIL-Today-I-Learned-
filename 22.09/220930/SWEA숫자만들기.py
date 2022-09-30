op = ['+', '-', '*', '/']

T = int(input())
for t in range(T):
    n = int(input())
    operate = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    operations_p = []
    operations_m = []
    for i in range(4):
        if i % 2:
            operations_m.extend([op[i] for _ in range(operate[i])])
        else:
            operations_p.extend([op[i] for _ in range(operate[i])])
