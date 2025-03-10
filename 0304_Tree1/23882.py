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
            stack.extend(tree[current])  # 현재 노드의 자식들을 쭉쭉 스택에 추가

    return cnt

T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())  # 간선 개수, 루트로 삼을 노드
    edges = list(map(int, input().split()))  # 부모-자식 관계 리스트

    tree = {}

    # 트리 구성
    for i in range(E):
        parent, child = edges[2 * i], edges[2 * i + 1]
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)

    result = count_subtree_size(tree, N)

    # 결과 출력
    print(f"#{t} {result}")