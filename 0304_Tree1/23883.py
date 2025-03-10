# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색

import sys
sys.stdin = open("23883.input.txt", "r")

def inorder_traversal(tree, node):
    if tree[node] == None:
        return
    if node in tree and tree[node]:  # 왼쪽 자식이 있으면 방문
        inorder_traversal(tree, tree[node][0])
    result.append(node)
    if node in tree and len(tree[node]) > 1:  # 오른쪽 자식이 있으면 방문
        inorder_traversal(tree, tree[node][1])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    tree = {}

    for parent in range(1, N + 1):
        tree[parent] = []
        if parent * 2 < N + 1:
            tree[parent].append(parent * 2)
        if parent * 2 + 1 < N + 1:
            tree[parent].append(parent * 2 + 1)

    result = []
    inorder_traversal(tree, 1)
    root = 1
    root_value = result.index(root) + 1  # 루트의 값 출력
    half = N//2
    half_value = result.index(half) + 1  # N의 절반의 값 출력

    print(f'#{tc} {root_value} {half_value}')