# [S/W 문제해결 응용] 4일차 - 보급로

import heapq
import sys
sys.stdin = open("1249.input.txt", "r")

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def min_repair_time(N, grid):
    repair_time = [[float('inf')] * N for _ in range(N)]
    repair_time[0][0] = grid[0][0]

    pq = [(grid[0][0], 0, 0)]

    while pq:
        time, x, y = heapq.heappop(pq)

        if time > repair_time[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_time = time + grid[nx][ny]
                if new_time < repair_time[nx][ny]:
                    repair_time[nx][ny] = new_time
                    heapq.heappush(pq, (new_time, nx, ny))

    return repair_time[N - 1][N - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    print(f'#{tc} {min_repair_time(N, grid)}')