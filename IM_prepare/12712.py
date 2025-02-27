# 파리퇴치3

import sys
sys.stdin = open("12712.input.txt", "r")

def catch_fly(N, M, arr):
    direction_1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우 하 상 좌
    direction_2 = [[-1, 1], [1, 1], [1, -1], [-1, -1]]  # 대각선

    max_sum = 0

    for i in range(N):
        for j in range(N):
            total = arr[i][j]
            for di, dj in direction_1:
                for k in range(M-1):
                    ni, nj = i + di * (k + 1), j + dj * (k + 1)
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            max_sum = max(total, max_sum)

            total = arr[i][j]
            for di, dj in direction_2:
                for k in range(M-1):
                    ni, nj = i + di * (k + 1), j + dj * (k + 1)
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]

            max_sum = max(total, max_sum)

    return max_sum

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N = 한변 길이, M = 방향 길이
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = catch_fly(N, M, arr)
    print(f'#{tc} {result}')