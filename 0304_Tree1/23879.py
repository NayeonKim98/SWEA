# Tree 연습문제 1. 전위 순회 (가장 먼저 풀기)

import sys
sys.stdin = open("23879.input.txt", "r")

def preorder_traversal(tree, node):
    print(node, end=" ")
    if node in tree:  # 재귀할 때, child 가 root 가 되어 반복
        for child in tree[node]:
            preorder_traversal(tree, child)

V = int(input())  # 정점 개수
edges = list(map(int, input().split()))

tree = {}  # parent 의 child 들을 담을 Tree
children = set()  # 자식 노드 추적 (루트 찾기용)

for i in range(V - 1):  # 간선은 정점보다 한 개 적음
    parent, child = edges[2 * i], edges[2 * i + 1]
    if parent not in tree:  # parent key 에 child 를 하나씩 담기
        tree[parent] = []
    tree[parent].append(child)
    children.add(child)  # child 다 set 에 넣고 루트 찾기

root = None
for node in range(1, V + 1):
    if node not in children:
        root = node
        break

preorder_traversal(tree, root)