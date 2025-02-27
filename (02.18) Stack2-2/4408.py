# 자기 방으로 돌아가기

import sys

sys.stdin = open("4408.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    corridor = [0] * 201  # 복도는 1~200번으로 변환하여 사용

    for _ in range(N):
        start, end = map(int, input().split())
        start = (start + 1) // 2  # 방 번호를 복도 번호로 변환
        end = (end + 1) // 2

        if start > end:  # 시작 방이 더 크면 swap
            start, end = end, start

        for i in range(start, end + 1):
            corridor[i] += 1  # 해당 복도 구간의 사용량 증가

    print(f"#{tc} {max(corridor)}")  # 최대로 겹친 구간이 최소 시간