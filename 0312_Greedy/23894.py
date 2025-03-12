# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합 (완전탐색)

import sys
sys.stdin = open("23894.input.txt", "r")

def recur(cnt, total):
    arr[0][0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split()))]

    used = [0] * (N + 1)
    min_sum = 0
    path = []

    recur(0, 0)
    print(f'#{tc} {min_sum}')