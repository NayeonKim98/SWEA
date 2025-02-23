# 진기의 최고급 붕어빵

from collections import deque

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\SWEA\(02.19) Queue-1\1860.input.txt", "r", encoding="utf-8")

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N: 손님 수, M: 붕어빵 만드는 시간, K: M초마다 만드는 붕어빵 개수
    arrived_time = sorted(map(int, input().split()))  # 손님 도착 시간을 정렬

    result = "Possible"
    for i in range(N):
        time = arrived_time[i]  # 현재 손님이 도착하는 시간
        available_bread = (time // M) * K - i  # time까지 만들어진 붕어빵 개수 - 이미 제공한 손님 수
        
        if available_bread <= 0:  # 손님에게 줄 붕어빵이 부족하면 Impossible
            result = "Impossible"
            break

    print(f"#{tc} {result}")