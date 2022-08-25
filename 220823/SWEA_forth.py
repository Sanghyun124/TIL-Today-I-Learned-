for t in range(int(input())):
    postfix = list(input().split())
    stack = []

    result = 0
    for x in postfix:
        if x.isdigit():
            stack.append(int(x))
        elif x == '+' and len(stack) >= 2:
            right = stack.pop()
            left = stack.pop()
            result = right + left
            stack.append(result)
        elif x == '*' and len(stack) >= 2:
            right = stack.pop()
            left = stack.pop()
            result = right * left
            stack.append(result)
        elif x == '-' and len(stack) >= 2:
            right = stack.pop()
            left = stack.pop()
            result = left -right
            stack.append(result)
        elif x == '/' and len(stack) >= 2:
            right = stack.pop()
            left = stack.pop()
            result = left // right
            stack.append(result)

        elif x == '.' and len(stack) == 1:
            result = stack.pop()
            print(f'#{t + 1} {result}')

        else:
            print(f'#{t + 1} error')
            break
