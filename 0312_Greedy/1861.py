# 정사각형 방

import sys
sys.stdin = open("1861.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    max_step = 0
    room_num = 0

    for i in range(N):
        for j in range(N):
            step_flag = 1
            step = 0
            while step_flag:
                ci, cj = i, j
                x, y = ci, cj
                for di, dj in direction:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ci][cj] + 1 == arr[ni][nj]:
                        step += 1
                        ci, cj = ni, nj
                        break

                if ci == x and cj == y:
                    step_flag = 0

            if step > max_step:
                max_step = step
                room_num = arr[i][j]

    print(f'#{tc} {room_num} {max_step}')