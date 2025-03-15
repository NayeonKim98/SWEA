# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색

import sys
sys.stdin = open("23883.input.txt", "r")

def in_order(idx, N):
    global cnt
    if idx <= N:  # 배열 범위 내에 있을 때까지 진행
        in_order(idx * 2, N)  # 왼쪽 자식 방문
        tree[idx] = cnt
        cnt += 1
        in_order(idx * 2 + 1, N)  # 오른쪽 자식 방문

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 1 ~ N 까지의 수를 저장

    tree = [0] * (N + 1)
    cnt = 1

    in_order(1, N)  # 중위 순회로 트리에 값 채우기

    root_value = tree[1]
    half_value = tree[N // 2]

    print(f'#{tc} {root_value} {half_value}')
