# 사각형 찾기(11039, sw)

import sys
sys.stdin = open("11039.input.txt", "r")

def find_square(N, arr):
    max_area = 0

    for ci in range(N):
        for cj in range(N):
            if arr[ci][cj] == 1:
                width = 1
                height = 1
                ni, nj = ci, cj

                while nj + 1 < N and arr[ni][nj + 1] == 1:
                    width += 1
                    nj += 1
                while ni + 1 < N and arr[ni+1][nj] == 1:
                    height += 1
                    ni += 1

                max_area = max(width * height, max_area)

    return max_area

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = find_square(N, arr)
    print(f'#{tc} {result}')