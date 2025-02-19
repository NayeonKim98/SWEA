# [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

import sys
sys.stdin = open("21618.input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    txt = input()

    top = -1
    stack = [0] * len(txt)

    for x in txt:
        top += 1                                # 일단 top 을 증가시키고
        stack[top] = x                          # 그 top 자리에 x 문자를 대체.

        if stack[top-1] == x:                   # 만약 x가 그 전 stack 의 문자와 같다면,
            stack[top] = 0                      # 둘 다 다시 0으로 대체.
            stack[top-1] = 0
            top -= 2                            # 그리고 원래 문자 자리로 top 을 옮김.

    print(f'#{tc} {top+1}')