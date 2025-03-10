# Tree 연습문제 1. 전위 순회 (가장 먼저 풀기)

import sys
sys.stdin = open("23879.input.txt", "r")

def preorder_traversal(tree, node):
    print(node, end=" ")  # 현재 노드 방문
    if node in tree:
        for child in tree[node]:  # 왼쪽부터 순서대로 방문
            preorder_traversal(tree, child)

V = int(input())
edges = list(map(int, input().split()))

tree = {}
children = set()  # 자식 노드 추적 (루트 찾기용)

for i in range(V - 1):
    parent, child = edges[2 * i], edges[2 * i + 1]
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)
    children.add(child)

# 루트 노드 찾기 (부모 노드 중에서 자식으로 등장하지 않은 노드 찾기)
root = None
for node in range(1, V + 1):
    if node not in children:
        root = node
        break

# 전위 순회 실행
preorder_traversal(tree, root)