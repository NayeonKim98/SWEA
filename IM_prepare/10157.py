# 자리배정(10157,bj)

def getSeat(C, R, K):
    arr = [[0]*C for _ in range(R)]
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    num = 1
    ci, cj = R - 1, 0
    arr[ci][cj] = num
    dir_idx = 0

    while num < K:
        if K > C * R:
            return 0
            break

        ni, nj = ci + directions[dir_idx][0], cj + directions[dir_idx][1]

        if not (0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 0):
            dir_idx = (dir_idx + 1) % 4
            ni, nj = ci + directions[dir_idx][0], cj + directions[dir_idx][1]

        ci, cj = ni, nj
        num += 1
        arr[ci][cj] = num

    return cj + 1, R - ci

C, R = map(int, input().split())  # C = 가로길이, R = 세로길이
K = int(input())  # K = 관객 번호

ans = getSeat(C, R, K)
print(" ".join(map(str, ans)))
