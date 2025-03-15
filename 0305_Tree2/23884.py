# [S/W 문제해결 기본] 9일차 - 사칙연산

import sys
sys.stdin = open("23884.input.txt", "r")

def evaluate_expression(tree, node):
    if len(tree[node]) == 1:  # 연산자 없는 노드의 경우 그대로 숫자 반환
        return tree[node][0]

    operator, left, right = tree[node]  # 연산자, 두 숫자 들어있는 경우
    left_value = evaluate_expression(tree, left)
    right_value = evaluate_expression(tree, right)

    # 사칙 연산
    if operator == '+':
        return left_value + right_value
    elif operator == '-':
        return left_value - right_value
    elif operator == '*':
        return left_value * right_value
    elif operator == '/':
        return left_value // right_value

T = 10
for tc in range(1, 11):
    N = int(input())

    tree = {}

    for _ in range(N):  # N 개 만큼 연산 정보
        edges = input().split()
        parent = int(edges[0])

        if len(edges) == 2:  # 연산자 없이 숫자만 받은 경우,
            tree[parent] = [int(edges[1])]
        else:  # 연산자, 두 수까지 받은 경우,
            operator = edges[1]
            left_child = int(edges[2])
            right_child = int(edges[3])
            tree[parent] = [operator, left_child, right_child]

    result = evaluate_expression(tree, 1)
    print(f'#{tc} {result}')