# Stack 1 - 연습문제 2. 괄호 검사 (가장 먼저 해결하기)

import sys
sys.stdin = open("21619.input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    txt = input()

    top = -1
    stack = [0] * len(txt)

    ans = 1
    for x in txt:
        if x in '{(':       # 여는 괄호면 stack 에 추가하고 top += 1
            top += 1
            stack[top] = x
        elif x in ')}':     # 닫는 괄호면 top -= 1 (쌍을 맞춰야 하니까)
            if top == -1:   # 근데 닫는 괄호를 발견했을 때, top 이 이미 -1이면 짝이 안맞는 거니까 ans = 0 (top = 0 이런식이어야함)
                ans = -1
                break
            if (x == ')' and stack[top] == '(') or (x == '}' and stack[top] == '{'):  # 짝이 맞으면 pop
                top -= 1    # else X 스택이 비어있지 않더라도 잘못된 짝일 때(예: {) 같은 경우) 처리 X
            else:           # 짝이 맞지 않으면 실패
                ans = -1
                break
    if top != -1:           # 다시 -1까지 돌아온게 아니라면
        ans = -1

    print(f'#{tc} {ans}')