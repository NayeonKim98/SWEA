# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

import sys
sys.stdin = open("22009.input.txt", "r")

# 부모 노드를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

# 두 노드를 연결
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V: 마지막 노드 번호, E: 간선 개수

    # 간선 정보 저장
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))  # 가중치를 맨 앞으로 (정렬 쉽게)

    edges.sort()  # 간선 가중치 기준으로 오름차순 정렬

    # Union-Find 를 위한 부모 배열
    parent = [i for i in range(V + 1)]

    total_weight = 0  # MST 총 가중치
    edge_count = 0  # MST에 포함된 간선 수

    for w, u, v in edges:
        # 사이클이 생기지 않으면 연결
        if find(u) != find(v):
            union(u, v)
            total_weight += w
            edge_count += 1

            # MST는 항상 V개의 노드에 대해 V개의 간선 - 1개만 필요함
            if edge_count == V:
                break

    print(f"#{tc} {total_weight}")