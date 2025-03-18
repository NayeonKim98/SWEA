# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

from collections import deque

import sys
sys.stdin = open("23899.input.txt", "r")

def min_charges(N, stops):
    queue = deque()
    queue.append((0, stops[0], 0))  # (현재 정류장, 남은 배터리, 교체 횟수)

    min_swaps = float('inf')  # 최소 교체 횟수 저장
    visited = {}  # (정류장, 남은 배터리) 상태 저장

    while queue:
        station, battery, swaps = queue.popleft()

        # 목적지 도달 시 최소 교체 횟수 갱신
        if station >= N - 1:
            min_swaps = min(min_swaps, swaps)
            continue

        # 이미 방문한 상태(정류장, 배터리 잔량)가 더 적은 교체 횟수로 도달했으면 스킵
        if (station, battery) in visited and visited[(station, battery)] <= swaps:
            continue

        visited[(station, battery)] = swaps

        # 현재 위치에서 "남은 배터리만큼" 앞으로 이동 (배터리 소모)
        if battery > 0:
            queue.append((station + 1, battery - 1, swaps))

        # 현재 위치에서 "배터리를 교체"하고 다시 최대 이동 가능
        queue.append((station + 1, stops[station] - 1, swaps + 1))  # 배터리 교체

    return min_swaps


T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]  # 정류장 개수
    stops = data[1:]  # 정류장 별 배터리 용량

    min_swaps = min_charges(N, stops)

    print(f'#{tc} {min_swaps}')