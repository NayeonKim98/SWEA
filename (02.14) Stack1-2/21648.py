# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

import sys
sys.stdin = open("21648.input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_arr = [[] for _ in range(V + 1)]

    for i in range(E):
        v, w = map(int, input().split())
        adj_arr[v].append(w)

    print(f'#{tc} {adj_arr}')