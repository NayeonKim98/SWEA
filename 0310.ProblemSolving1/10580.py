# 전봇대

import sys
sys.stdin = open("10580.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pole = [list(map(int, input().split())) for _ in range(N)]
    cross_count = 0

    pole.sort()

    for i in range(N):
        for j in range(i+1, N):
            if pole[i][1] > pole[j][1]:  # A로 정렬된 상태에서(오름차순) 앞쪽의 B가 뒷쪽보다 크면 교차가 생김.
                cross_count += 1

    print(f'#{tc} {cross_count}')