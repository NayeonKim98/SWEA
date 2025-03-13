# 부분 집합 합 구하기

import sys
sys.stdin = open("1487.input.txt","r")

T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(1, 1 << N):  # 모든 부분집합을 생성
        subset_sum = 0
        for j in range(N):
            if i & (1 << j):
                subset_sum += arr[j]
        if subset_sum == S:
            count += 1

    print(count)