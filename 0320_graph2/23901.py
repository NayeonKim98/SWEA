# 5250. [파이썬 S/W 문제해결 구현] - 최소 비용

import heapq
import sys
sys.stdin = open("23901.input.txt", "r")

# 다익스트라 알고리즘
def dijkstra(matrix, N):
    MAX = float('inf')  # 초기 거리
    dist = [[MAX] * N for _ in range(N)]  # 거리 정보 저장 배열
    dist[0][0] = 0  # 시작점의 연료 소모량 0
    pq = [(0, 0, 0)]  # (연료, x, y)
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 4방향 이동

    while pq:
        fuel, x, y = heapq.heappop(pq)

        # 이미 더 적은 연료로 방문했다면 스킵
        if fuel > dist[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 매트릭스 범위 안에 들어오는 경우만 처리
            if 0 <= nx < N and 0 <= ny < N:
                height_diff = matrix[nx][ny] - matrix[x][y]
                extra_fuel = height_diff if height_diff > 0 else 0
                new_fuel = fuel + 1 + extra_fuel  # 기본 연료 1 + 높이차 연료

                # 최소 연료 갱신 시 큐에 추가
                if new_fuel < dist[nx][ny]:
                    dist[nx][ny] = new_fuel
                    heapq.heappush(pq, (new_fuel, nx, ny))

    return dist[N - 1][N - 1]  # 도착지점까지 최소 연료 반환

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra(matrix, N)
    print(f"#{tc} {result}")
