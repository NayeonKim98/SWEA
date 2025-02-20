# 진기의 최고급 붕어빵

from collections import deque

import sys
sys.stdin = open("1860.input.txt", "r")

T = int(input())
for tc in range(1, 30+1):
    N, M, K = map(int, input().split())
    arrived_time = list(map(int, input().split()))
    arrived_time_sorted = deque(sorted(arrived_time))

    result = 'Possible'
    original_K = K

    print(f'{N} {M} {K}')
    print(arrived_time_sorted)

    # K 개 만큼 만들었으면 0~K-1번 인덱스까지의 사람들 남은 시간 - M (que의 숫자들은 도착한 시간임!!!!!!!!!!)

    while N > 0:                        # 먹을 수 있는 사람이 남아있을 때까지
        if arrived_time_sorted[0] - M >= 0:    # 도착을 굽는 시간보다 더 늦게 하면
            N -= 1                      # 먹을 수 있는 사람 감소
            K -= 1                      # 만든 붕어빵 개수 감소
            arrived_time_sorted.popleft()   # 먹은사람 퇴장
            if K == 0:                  # 만약
                K = original_K
        else:                           # 도착 시간이 붕어빵 만드는 시간을 넘어서면
            result = 'Impossible'
            break

    if len(arrived_time_sorted) != 0:
        result = 'Impossible'

    print(f'#{tc} {result}')