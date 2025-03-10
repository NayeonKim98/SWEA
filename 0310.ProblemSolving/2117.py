# [모의 SW 역량테스트] 홈 방범 서비스

import sys
sys.stdin = open("2117.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_house = 0

    for K in range(1, N + 2):
        cost = K * K + (K - 1) * (K - 1)

        for ci in range(N):
            for cj in range(N):
                total_house = 0

                # 마름모 범위 내에 있는 집을 카운트
                for i in range(N):
                    for j in range(N):
                        if abs(i - ci) + abs(j - cj) < K:  # 마름모 범위 내인지 확인 ( 거리 K 미만으로 닿아야함 )
                            total_house += arr[i][j]

                revenue = total_house * M
                profit = revenue - cost

                if profit >= 0:
                    max_house = max(max_house, total_house)
        K += 1

    print(f'#{tc} {max_house}')