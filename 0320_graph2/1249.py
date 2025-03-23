# [S/W 문제해결 응용] 4일차 - 보급로

import heapq
import sys
sys.stdin = open("1249.input.txt", "r")

# 이동 방향(우, 하, 좌, 상)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 다익스트라 - 최소 복구 시간
def dijkstra(N, grid):
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0  # 시작점 복구 시간 = 0
    pq = [(0, 0, 0)]  # (복구 시간, x, y)

    while pq:
        cost, x, y = heapq.heappop(pq)

        # 이미 더 짧은 경로로 왔으면 스킵
        if dist[x][y] < cost:
            continue

        for d in range(4):
            nx, ny = x + di[d], y + dj[d]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + int(grid[nx][ny])
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))

    return dist[N - 1][N - 1]  # 도착점 복구시간 반환

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [input().strip() for _ in range(N)]
    answer = dijkstra(N, grid)
    print(f"#{tc} {answer}")