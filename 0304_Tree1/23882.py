# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree

import sys
sys.stdin = open("23882.input.txt", "r")

def count_subtree_size(tree, node):
    stack = [node]
    cnt = 0

    while stack:
        current = stack.pop()
        cnt += 1
        if current in tree:
            stack.extend(tree[current])

    return cnt

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # 간선 개수, 루트로 삼을 노드
    edges = list(map(int, input().split()))

    tree = {}

    # 트리 구성
    for i in range(E):  # 간선 개수 만큼
        parent, child = edges[2 * i], edges[2 * i + 1]
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)

    result = count_subtree_size(tree, N)
    print(f'#{tc} {result}')