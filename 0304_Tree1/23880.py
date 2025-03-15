# [S/W 문제해결 기본] 9일차 - 중위순회

import sys
sys.stdin = open("23880.input.txt", "r")

def in_order(tree, node):
    if node in tree and len(tree[node]) > 1:  # 주어진 노드가 tree에 있고, 자식이 있으면,
        in_order(tree, tree[node][1])  # 왼쪽 자식 방문
    print(tree[node][0], end="")  # 그 단어 출력
    if node in tree and len(tree[node]) > 2:  # 오른쪽 자식이 있으면 방문
        in_order(tree, tree[node][2])

T = 10
for tc in range(1, 11):
    N = int(input())  # 정점의 개수

    tree = {}
    children = set()

    for _ in range(N):
        edges = list(map(str, input().split()))  # 1 W 2 3 이런 부모, 단어, 자식들 형식
        parent = int(edges[0])  # 첫 번째가 부모
        if parent not in tree:
            tree[parent] = []
        char = edges[1]  # 두 번째가 글자
        tree[parent].append(char)
        for j in range(2, len(edges)):  # 세 번째 부터는 자식
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
    in_order(tree, root)  # 중위 순회 실행
    print()