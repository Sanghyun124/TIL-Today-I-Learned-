icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}


def get_postfix(infix, n):
    postfix = ''
    stack = []

    for i in range(n):
        if '0' <= infix[i] <= '9':
            postfix += infix[i]
        else:
            # 연산자가 닫는 괄호일 경우 ==> 여는 괄호가 나올때까지 연산자를 모두 pop
            # 괄호가 아닐 경우 => 자기 자신이 스택안에 있는 것보다 우선순위가 높아질 때 까지 pop
            if infix[i] == ')':
                while stack:
                    char = stack.pop()
                    if char == '(':
                        break
                    postfix += char

            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                # 내 우선순위가 높거나 스택 안에 아무것도 남지 않았다. ==> push
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()
    return postfix


def get_result(postfix):
    stack = []

    for c in postfix:
        if '0' <= c <= '9':
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()

        if c == '+':
            result = left + right
        elif c == '-':
            result = left - right
        elif c == '*':
            result = left * right
        elif c == '-':
            result = left / right

        stack.append(result)

    return stack.pop()
