# 격자판의 숫자 이어 붙이기

import sys
sys.stdin = open("2819.input.txt", "r")

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, num, depth, grid, unique_numbers):
    if depth == 6:  # 7자리 숫자가 완성되면 set에 추가
        unique_numbers.add(num)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:  # 격자 내에 있을 때만 이동
            dfs(nx, ny, num * 10 + grid[nx][ny], depth + 1, grid, unique_numbers)


def count_unique_numbers(grid):
    unique_numbers = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, grid[i][j], 0, grid, unique_numbers)  # 각 점에서 DFS 시작
    return len(unique_numbers)


T = int(input())
for t in range(1, T + 1):
    grid = [list(map(int, input().split())) for _ in range(4)]
    result = count_unique_numbers(grid)
    print(f"#{t} {result}")
