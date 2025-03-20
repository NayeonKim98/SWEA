# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

import sys
sys.stdin = open("22009.input.txt", "r")

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a, root_b = find(parent, a), find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a

def kruskal(V, edges):
    parent = list(range(V + 1))
    edges.sort(key=lambda x: x[2])
    mst_cost, count = 0, 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_cost += w
            count += 1
            if count == V:
                break

    return mst_cost

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]

    print(f'#{tc} {kruskal(V, edges)}')