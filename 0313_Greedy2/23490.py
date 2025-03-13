# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

import sys
sys.stdin = open("23490.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    trucks = [tuple(map(int, input().split())) for _ in range(N)]

    trucks.sort(key=lambda x: x[1])  # 끝나는 시간 순서로 정렬

    count = 0
    last_end = 0

    for s, e in trucks:  # 시작시간, 끝나는 시간
        if s >= last_end:
            count += 1
            last_end = e

    print(f'#{tc} {count}')