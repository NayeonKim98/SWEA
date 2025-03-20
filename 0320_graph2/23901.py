# 5250. [파이썬 S/W 문제해결 구현] - 최소 비용

import heapq
import sys
sys.stdin = open("23901.input.txt", "r")

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상, 하, 좌, 우 방향 벡터

def min_fuel_consumption(grid):
    inf = float('inf')

    fuel_cost = [[inf] * N for _ in range(N)]
    fuel_cost[0][0] = 0

    heap = [(0, 0, 0)]  # (연료 소비량, x좌표, y좌표)

    while heap:
        cost, x, y = heapq.heappop(heap)

        if cost > fuel_cost[x][y]:  # 꺼낸 비용이 기존보다 크면 무시
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                additional_cost = max(0, grid[nx][ny] - grid[x][y])
                new_cost = cost + 1 + additional_cost  # 높이 차이도 비용에 고려

                if new_cost < fuel_cost[nx][ny]:  # 더 적은 연료 가능이면 업데이트
                    fuel_cost[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return fuel_cost[N - 1][N - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {min_fuel_consumption(grid)}')
