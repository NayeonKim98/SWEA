# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

import sys
sys.stdin = open("23488.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    total_weight = 0
    truck_index = 0

    for weight in containers:
        if truck_index < M and trucks[truck_index] >= weight:
            total_weight += weight
            truck_index += 1

    print(f'#{tc} {total_weight}')