# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

import heapq
import sys
sys.stdin = open("22011.input.txt", "r")

# 다익스트라 알고리즘
def dijkstra(start, graph, N):
    INF = float('inf')
    distance = [INF] * (N + 1)  # 거리 리스트
    distance[start] = 0  # 시작점의 거리 0

    # 최소 힙을 이용한 우선순위 큐
    heap = []
    heapq.heappush(heap, (0, start))  # (거리, 노드번호) 형태로 push

    while heap:
        dist, now = heapq.heappop(heap)  # 가장 짧은 거리의 노드 꺼냄

        # 이미 처리된 노드라면 무시
        if distance[now] < dist:  # 지금 뽑은 거리보다 원래 거리가 더 짧으면
            continue

        # 인접 노드 확인
        for next_node, weight in graph[now]:
            cost = dist + weight  # 현재 노드까지 거리 + 다음 노드까지 거리
            if cost < distance[next_node]:  # 더 짧은 경로라면 갱신
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

    return distance[N]  # 0번에서 N번까지의 최소 거리 반환


# 테스트 케이스 수 입력
T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())  # 마지막 노드 번호 N, 도로 수 E

    # 인접 리스트 방식
    graph = [[] for _ in range(N + 1)]

    # 간선 정보 입력 받기
    for _ in range(E):
        s, e, w = map(int, input().split())  # 시작점(start), 도착점(end), 거리(weight)
        graph[s].append((e, w))  # 방향성이 있으므로 s → e 만 추가

    # 다익스트라 알고리즘 실행
    min_distance = dijkstra(0, graph, N)

    # 결과 출력
    print(f"#{tc} {min_distance}")
