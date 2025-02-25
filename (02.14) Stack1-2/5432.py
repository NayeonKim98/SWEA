# 쇠막대기 자르기

import sys

sys.stdin = open("5432.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    arr = input()
    stack = []
    count = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append('(')
        else:  # 닫는 괄호면
            stack.pop()
            if arr[i-1] == '(':
                count += len(stack)  # 레이저면 현재 스택에 쌓인 개수만큼 증가
            else:  # 그 전도 닫는 괄호면 쇠막대기가 끝인거니까
                count += 1  # arr[i-1] 이후 막대 끝나니까 1개씩 추가

    print(f'#{tc} {count}')