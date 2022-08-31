T = 10
for tc in range(1, T + 1):
    n = int(input())

    exp = input()
    postfix = ''
    stack = []

    icp = {'+': 1, '*': 2}

    for i in range(n):
        if '0' <= exp[i] <= '9':
            postfix += exp[i]
        else:
            # 연산자면 스택의 꼭대기(top)을 확인해서
            # 자신보다 같거나 높은 우선순위를 가진 연산자가 있으면 꺼낸다.
            if stack and icp[stack[-1]] >= icp[exp[i]]:
                postfix += stack.pop()
                stack.append(exp[i])

    while stack:
        postfix += stack.pop()

    result = 0  # 저장결과

    stack = []
    k = len(postfix)
    for i in range(k):
        # 피연산자가 나오면 그냥 넘어가고(스택에 담는다)
        # 연산자가 나오면 계산(스택에서 두개의 피연산자를 꺼낸다)
        if '0' <= exp[i] <= '9':
            stack.append(postfix[i])
        else:
            right = int(stack.pop())
            left = int(stack.pop())

            if postfix[i] == '+':
                result = right + left
            else:
                result = right * left

            stack.append(result)

    print(f'#{tc} {result}')
