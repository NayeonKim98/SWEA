# [S/W 문제해결 응용] 4일차 - 하나로

import sys
sys.stdin = open("1251.input.txt", "r")

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a, root_b = find(parent, a), find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            d = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            edges.append((d * E, i, j))

    edges.sort()
    parent = list(range(N))
    cost, cnt = 0, 0

    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            cost += w
            cnt += 1
            if cnt == N - 1:
                break

    print(f'#{tc} {round(cost)}')