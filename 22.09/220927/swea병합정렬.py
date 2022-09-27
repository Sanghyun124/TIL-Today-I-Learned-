from collections import deque

def merge_sort(ary):
    size=len(ary)
    if size == 1:
        return ary
    left = deque()
    right = deque()
    for _ in range(size//2):
        left.append(ary.popleft())
    for _ in range(size//2,size):
        right.append(ary.popleft())


    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global count
    result = deque()
    count += 1 if left[-1] > right[-1] else 0
    while left or right:
        if left and right:
            if left[0] > right[0]:
                result.append(right.popleft())
            else:
                result.append(left.popleft())
        elif left:
            result.append(left.popleft())
        elif right:
            result.append(right.popleft())
    return result


T = int(input())
for t in range(T):
    n = int(input())
    ary = deque(list(map(int, input().split())))
    count = 0
    result = merge_sort(ary)
    print(f'#{t + 1} {result[n // 2]} {count}')