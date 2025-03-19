# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

import sys
sys.stdin = open("23900.input.txt", "r")

from collections import deque

def min_operations(N, M):
    dp = [-1] * 1000001  # dp[i] = i까지 가는 최소 연산 횟수 (최소니까..inf로 해야하나..?)
    queue = deque([N])
    dp[N] = 0  # 시작점 step 0에서 출발

    while queue:
        num = queue.popleft()
        steps = dp[num]

        if num == M:
            return steps

        # 가능한 연산들
        for next_num in (num + 1, num - 1, num * 2, num - 10):
            if 1 <= next_num <= 1000000 and dp[next_num] == -1:  # 범위 100만 이하
                dp[next_num] = steps + 1  # 최소 연산 횟수 갱신
                queue.append(next_num)

    return -1  # 도달 불가능한 경우는 없음

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = min_operations(N, M)

    print(f'#{tc} {answer}')