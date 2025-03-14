# 물놀이를 가자

import sys
sys.stdin = open("10966.input.txt", "r")

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def multi_source_bfs(N, M, grid):
    from collections import deque

    q = deque()
    distances = [[-1] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'W':
                q.append((i, j, 0))  # 좌표와 현재 거리
                distances[i][j] += 1  # 물인 곳은 거리 0

    total_distance = 0

    while q:
        x, y, dist = q.popleft()

        for di, dj in directions:
            ni, nj = x + di, y + dj
            if 0 <= ni < N and 0 <= nj < M and distances[ni][nj] == -1:  # 방문하지 않은 범위 내의 곳일 때,
                if grid[ni][nj] == 'L':  # 그 곳이 땅이면 거리를 추가.
                    distances[ni][nj] = dist + 1
                    total_distance += dist + 1
                    q.append((ni, nj, dist + 1))

    return total_distance

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]

    result = multi_source_bfs(N, M, grid)
    print(f'#{tc} {result}')