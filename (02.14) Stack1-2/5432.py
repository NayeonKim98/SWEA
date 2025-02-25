# 쇠막대기 자르기

import sys

sys.stdin = open("5432.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    arr = input().strip()
    stack = []
    count = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append('(')  # 쇠막대기 시작
        else:  # 닫는 괄호 `)`
            stack.pop()  # 쇠막대기 끝 처리
            if arr[i - 1] == '(':  # 레이저라면
                count += len(stack)  # 현재 스택에 쌓인 쇠막대기 개수만큼 추가
            else:  # 쇠막대기 끝이라면
                count += 1  # 막대기가 끝났으므로 조각 1개 추가

    print(f'#{tc} {count}')