# [S/W 문제해결 기본] 9일차 - 사칙연산

import sys
sys.stdin = open("23884.input.txt", "r")

def inorder_traversal(tree, node):
    if node in tree and len(tree[node]) == 3:  # 왼쪽 자식이 있으면 방문
        inorder_traversal(tree, tree[node][1])
    result.append(node)
    if node in tree and len(tree[node]) == 3:  # 오른쪽 자식이 있으면 방문
        inorder_traversal(tree, tree[node][2])

T = 10
for tc in range(1, 11):
    N = int(input())

    tree = {}

    for _ in range(N):  # 간선의 개수는 V - 1
        edges = list(map(str, input().split()))
        parent = int(edges[0])  # 첫번째 원소가 부모
        if parent not in tree:
            tree[parent] = []
        if len(edges) == 4:
            operator = edges[1]  # 사칙연산 따로 저장
            tree[parent].append(operator)
            # 연산 필요한 애들은 따로 저장
            for j in range(2, len(edges)):
                child = edges[j]
                tree[parent].append(int(child))
        else:  # 부모랑 숫자만 있으면 그냥 저장
            child = edges[1]
            tree[parent].append(int(child))

    result = []
    stack = []
    inorder_traversal(tree, 1)
    for num in result:
        for j in range(len(tree[num])):
            if type(tree[num][j]) == int:
                stack.append(tree[num][j])
            elif type(tree[num][j]) == str:
                pass

    print(result)