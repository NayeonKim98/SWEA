# [S/W 문제해결 기본] 7일차 - 미로2
from collections import deque

import sys
sys.stdin = open("1227.input.txt", "r")

def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        ti, tj = q.popleft()

        if maze[ti][tj] == 3:
            return 1

        for di, dj in directions:
            wi , wj = ti + di, tj + dj

            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append((wi, wj))
                visited[wi][wj] = 1

    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = 10
for tc in range(1, T+1):
    test_case = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    sti, stj = find_start(100)
    ans = bfs(sti, stj, 100)

    print(f"#{test_case} {ans}")