# [S/W 문제해결 응용] 4일차 - 하나로

import heapq
import sys
sys.stdin = open("1251.input.txt", "r")

def prim():
    pq = [(0, 0)]  # (비용, 노드)
    visited = [False] * N  # 방문 체크
    min_cost = 0  # 최소 환경 부담금 (누적)

    # 각 노드로 가는 최소 비용 저장 리스트
    dists = [float('inf')] * N
    dists[0] = 0  # 시작 노드는 비용 0

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node]:  # 이미 연결된 노드면 패스
            continue

        visited[node] = True  # 방문 처리
        min_cost += cost  # 비용 누적

        for next_node in range(N):
            if visited[next_node]:
                continue

            # 거리 계산 (유클리드 거리의 제곱)
            dx = x_li[next_node] - x_li[node]
            dy = y_li[next_node] - y_li[node]
            new_cost = (dx * dx + dy * dy) * E

            # 더 저렴한 비용이면 갱신 및 큐에 push
            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return round(min_cost)  # 소수 첫째 자리에서 반올림

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 섬 개수
    x_li = list(map(int, input().split()))  # X좌표 리스트
    y_li = list(map(int, input().split()))  # Y좌표 리스트
    E = float(input())  # 환경 부담 세율

    ans = prim()
    print(f"#{tc} {ans}")
