# [S/W 문제해결 기본] 9일차 - 중위순회

import sys
sys.stdin = open("23880.input.txt", "r")

def in_order(tree, node):
    if node in tree and len(tree[node]) > 1:
        in_order(tree, tree[node][1])  # 자식있는 왼쪽 노드 방문
    print(tree[node][0], end="")
    if node in tree and len(tree[node]) > 2:
        in_order(tree, tree[node][2])

T = 10
for tc in range(1, 11):
    N = int(input())

    tree = {}
    children = set()

    for _ in range(N):  # 간선의 개수는 V - 1
        edges = list(map(str, input().split()))
        parent = int(edges[0])  # 두번째 원소가 부모
        if parent not in tree:
            tree[parent] = []
        char = edges[1]  # 문자 따로 저장
        tree[parent].append(char)
        for j in range(2, len(edges)):
            child = edges[j]
            tree[parent].append(int(child))
            children.add(int(child))

    # 루트 노드 찾기
    root = None
    for node in range(1, N + 1):
        if node not in children:
            root = node
            break

    print(f'#{tc}', end=" ")
    # 중위 순회 실행
    in_order(tree, root)
    print()