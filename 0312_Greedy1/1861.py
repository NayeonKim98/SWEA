# 정사각형 방

import sys
sys.stdin = open("1861.input.txt", "r")
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if dp[x][y] != -1:  # 이미 탐색했다 => 바로 반환(메모제이션)
        return dp[x][y]

    dp[x][y] = 1  # 최소한 자기 자신 방문

    for direction in range(4):
        ni, nj = x + dx[direction], y + dy[direction]

        if 0 <= ni < N and 0 <= nj < N and room_grid[ni][nj] == room_grid[x][y] + 1:
            dp[x][y] = max(dp[x][y], 1 + dfs(ni, nj))  # 이동 횟수 1회씩 증가하기 때문에

    return dp[x][y]

def find_longest_path(N, room_grid):
    global dp
    dp = [[-1] * N for _ in range(N)]  # DP테이블 (메모제이션. -1로 초기화해놈)

    max_moves = 0
    best_start_room = float('inf')

    for row in range(N):
        for col in range(N):
            moves = dfs(row, col)  # (row, col)에서 시작했을 때 최대 이동 거리 계산

            if moves > max_moves or (moves == max_moves and room_grid[row][col] < best_start_room):
                max_moves = moves
                best_start_room = room_grid[row][col]

    return best_start_room, max_moves

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room_grid = [list(map(int, input().split())) for _ in range(N)]

    start_room, move_count = find_longest_path(N, room_grid)

    print(f'#{tc} {start_room} {move_count}')

# # 정사각형 방
#
# import sys
# sys.stdin = open("1861.input.txt", "r")
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def find_longest_path(N, room_grid):
#     position_map = {}  # 숫자가 적힌 위치를 빠르게 탐색.
#     for row in range(N):
#         for col in range(N):
#             position_map[room_grid[row][col]] = (row, col)
#
#     max_moves = 0
#     best_start_room = float('inf')
#
#     for room_number in range(1, N*N + 1):
#         if room_number in position_map:  # 해당 숫자가 존재하면
#             x, y = position_map[room_number]  # 그 위치를 불러옴
#             current_moves = 1
#
#             while True:
#                 can_move = False  # 이동 가능한지 여부
#
#                 for direction in range(4):
#                     ni, nj = x + dx[direction], y + dy[direction]
#
#                     if 0 <= ni < N and 0 <= nj < N and room_grid[ni][nj] == room_grid[x][y] + 1:
#                         x, y = ni, nj
#                         current_moves += 1
#                         can_move = True
#                         break
#
#                 if not can_move:
#                     break
#
#             if current_moves > max_moves or (current_moves == max_moves and room_number < best_start_room):
#                 max_moves = current_moves
#                 best_start_room = room_number
#
#     return best_start_room, max_moves
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     room_grid = [list(map(int, input().split())) for _ in range(N)]
#
#     # 가장 많이 이동할 수 있는 방 번호 / 이동 횟수 찾기
#     start_room, move_count = find_longest_path(N, room_grid)
#
#     print(f'#{tc} {start_room} {move_count}')