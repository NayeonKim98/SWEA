# [S/W 문제해결 기본] 7일차 - 미로1
from collections import deque

import sys
sys.stdin = open("1226.input.txt", "r")

# bfs 수행하여 도달 가능 여부를 판단
def bfs(i, j, N):   # 출발점과 미로판 길이를 받고,
    visited = [[0]*N for _ in range(N)]     # 방문 여부 저장
    q = deque()                             # 큐 생성
    q.append((i, j))                        # 시작점 인큐
    print(f"처음 큐 : {q}")
    visited[i][j] = 1                       # 시작점 방문 표시
    print(f"처음 방문 리스트 : {visited}")
    # 이동방향 (우, 하, 좌, 상)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # BFS 탐색 시작
    while q:    # q에 자료가 없어지기 직전까지
        ti, tj = q.popleft()

        if maze[ti][tj] == 3:   # 도착점(3)에 도달하면
            return 1            # 도달 가능하다라는 것을 반환

        for di, dj in directions:
            wi, wj = ti + di, tj + dj

            # 미로 범위 내, 벽이 아니고, 방문하지 않은 곳이라면,
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append((wi, wj))  # 큐에 다음 방문지점 추가하고
                print(f"방문 큐 : {q}")
                visited[wi][wj] = 1 # 방문했다고 표시
                print(f"방문 리스트 : {visited}")

    return 0

# 출발점(2)의 위치를 찾는 함수
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = 10
for tc in range(1,11):
    test_case = int(input())
    maze = list(list(map(int, input())) for _ in range(16))

    sti, stj = find_start(16)   # 출발점 찾음. 출발점의 i , j 설정.
    ans = bfs(sti, stj, 16)

    print(f'#{test_case} {ans}')