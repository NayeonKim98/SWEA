# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
from collections import deque

import sys
sys.stdin = open("21674.input.txt", "r")

def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((sti, stj))
    visited[sti][stj] = 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        ci, cj = q.popleft()

        if maze[ci][cj] == 3:
            return 1

        for di, dj in directions:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
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
    ans = bfs(sti, stj, N)

    print(f'#{tc} {ans}')