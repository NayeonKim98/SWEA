# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 (완전탐색)

import sys
sys.stdin = open("23894.input.txt", "r")

def dfs(x, y, current_sum):
    global min_sum

    if x == N - 1 and y == N - 1:
        if current_sum < min_sum:
            min_sum = current_sum
        return  # 끝까지 왔을 때 최소합을 갱신하고 다시 돌아가기

    if current_sum >= min_sum:
        return  # 합이 이미 최소합을 넘어섰으면 탐색할 필요가 없음 (가지치기)

    for di, dj in [(1, 0), (0, 1)]:
        ni, nj = x + di, y + dj
        if 0 <= ni < N and 0 <= nj < N:
            dfs(ni, nj, current_sum + grid[ni][nj])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')
    dfs(0, 0, grid[0][0])

    print(f'#{tc} {min_sum}')