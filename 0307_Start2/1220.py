#[S/W 문제해결 기본] 5일차 - Magnetic

import sys
sys.stdin = open("1220.input.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    print(table)

    for j in range(N):
        for i in range(N):
            if table[i][j] == 1:
                isRed = True