# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

import heapq
import sys
sys.stdin = open("22011.input.txt", "r")

def dijkstra(n, edges):
    adj = [[] for _ in range(n + 1)]
    for s, e, w in edges:
        adj[s].append((e, w))  # 단방향

    inf = float('inf')
    dist = [inf] * (n + 1)
    dist[0] = 0  # 시작 정점의 거리 = 0

    heap = [(0, 0)]  # (거리, 노드)

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        if cur_dist > dist[cur_node]:  # 이미 최소 거리가 계산되있는 경우는 스킵
            continue

        for next_node, weight in adj[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < dist[next_node]:  # 방문 안한 경우만
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return dist[n]

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    edges = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    shortest_path = dijkstra(N, edges)
    print(f'#{tc} {shortest_path}')