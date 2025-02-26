# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

import sys

sys.stdin = open("21675.input.txt", "r")


def evaluate_postfix(expression):
    calc_stack = []

    for e in expression:
        if e.isdigit():
            calc_stack.append(int(e))
        elif e in ('+', '-', '*', '/'):
            if len(calc_stack) < 2:  # 피연산자가 부족하면 오류
                return "error"

            num2 = calc_stack.pop()
            num1 = calc_stack.pop()

            if e == '+':
                calc_stack.append(num1 + num2)
            elif e == '-':
                calc_stack.append(num1 - num2)
            elif e == '*':
                calc_stack.append(num1 * num2)
            elif e == '/':
                if num2 == 0:  # 0으로 나누기 방지
                    return "error"
                calc_stack.append(num1 // num2)
        else:
            return "error"

    return calc_stack.pop() if len(calc_stack) == 1 else "error"


T = int(input())
for tc in range(1, T + 1):
    expression = input().split()

    # 마지막에 "."이 있으면 제거 (Forth 표기법)
    if expression[-1] == ".":
        expression.pop()

    result = evaluate_postfix(expression)
    print(f'#{tc} {result}')