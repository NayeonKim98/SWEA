# Stack 2 - 연습문제 1 - 후위 유사 표기법 연습 (가장 먼저 해결)

import sys
sys.stdin = open("21673.input.txt", "r")

precedence = {
    '+': 1,
    '*': 2,
    '/': 2
}

T = int(input())
for tc in range(1, T+1):
    expression = input()

    postfix = []
    stack = []

    for e in expression:
        if e.isdigit():
            postfix.append(e)
        else:
            if stack and precedence[stack[-1]] >= precedence[e]:
                postfix.append(stack.pop())
            stack.append(e)

    while stack:
        postfix.append(stack.pop())

    result = ''.join(postfix)
    print(f'#{tc} {result}')