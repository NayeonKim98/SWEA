#[S/W 문제해결 기본] 5일차 - Magnetic

import sys
sys.stdin = open("1220.input.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for j in range(N):
        isRed = False  # j열을 돌 때마다 False로 초기화시켜줘야함. (새로 count)
        for i in range(N):
            if table[i][j] == 1:  # 만약 열부터 순회하면서 N극을 보면, flag를 세움
                isRed = True
            elif table[i][j] == 2:  # 만약 S극을 보면, 그 전에 True였으면 flag 내리고 카운트 (충돌)
                if isRed == True:
                    count += 1
                    isRed = False

    print(f'#{tc} {count}')