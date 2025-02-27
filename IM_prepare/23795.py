# 우주 괴물(23795,sw)

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\SWEA\IM_prepare\23795.input.txt", "r", encoding="utf-8")


def shootlazer(N, arr):
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                ci, cj = i, j

    for di, dj in direction:
        for k in range(N):
            ni, nj = ci + di * (k + 1), cj + dj * (k + 1)
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                break
            elif 0 <= ni < N and 0 <= nj < N:
                arr[ni][nj] = 2

    return arr

def find_safe_area(N, arr):
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                count += 1

    return count

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    attacked_arr = shootlazer(N, arr)
    count = find_safe_area(N, attacked_arr)
    print(f'#{tc} {count}')