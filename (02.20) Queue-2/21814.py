# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

from collections import deque

import sys
sys.stdin = open("21814.input.txt", "r")

def bfs(i, j, N):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((i, j))
    visited[i][j] = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        ci, cj = q.popleft()

        if maze[ci][cj] == 3:
            return visited[ci][cj] - 1  # 출발지점까지 더해버렸으니 다시 하나 빼줘야함.

        for di, dj in directions:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == -1:  # maze[ni][nj] != 1 이건 벽 피하기위함, 출구는 가야하니까
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = find_start(N)
    result = bfs(sti, stj, N)

    print(f'#{tc} {result}')