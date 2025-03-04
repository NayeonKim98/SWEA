# [S/W 문제해결 기본] 6일차 - 계산기2

precedence = {
    '+': 1,
    '*': 2
}

T = 10
for tc in range(1, 11):
    num = int(input())
    equation = input()

    postfix = []
    stack = []

    # 후위표기식으로 만들기
    for e in equation:
        if e.isdigit():
            postfix.append(e)
        else:
            while stack and precedence[stack[-1]] >= precedence[e]:  # while stack : 이미 연산자가 1개 들어있으면 발동
                postfix.append(stack.pop())
            stack.append(e)  # 연산자 우선순위 더 높으면 그냥 추가

    while stack:  # 마지막에 숫자로 끝나서 stack에 연산자가 아직 남아있을 수 있으니까
        postfix.append(stack.pop())

    # 후위표기식을 계산하기
    calc_stack = []
    for e in postfix:
        if e.isdigit():
            calc_stack.append(int(e))
        else:
            num2 = calc_stack.pop()
            num1 = calc_stack.pop()

            if e == '+':
                calc_stack.append(num1 + num2)
            elif e == '*':
                calc_stack.append(num1 * num2)

    print(f'#{tc} {calc_stack.pop()}')