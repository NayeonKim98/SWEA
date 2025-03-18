# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

import sys
sys.stdin = open("23899.input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N, battery_capacity = data[0], data[1:]  # N: 정류장 개수, battery_capacity: 각 정류장의 배터리 용량 리스트

    swap_count = -1  # 배터리 교체 횟수
    current_position = N - 1  # 목표 정류장

    while current_position > 0:
        previous_position = 0  # 가장 멀리 이동할 수 있는 정류장 인덱스

        # 역방향으로 탐색하면서 현재 위치까지 도달할 수 있는 최적의 정류장 찾기
        for i in range(current_position - 1, -1, -1):
            if battery_capacity[i] >= current_position - i:  # 배터리 크기가 거리 차이보다 크면 이동 가능
                previous_position = i

        current_position = previous_position  # 최적 정류장으로 이동
        swap_count += 1  # 배터리 교체 횟수 증가

    print(f"#{tc} {swap_count}")
