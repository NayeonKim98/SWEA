# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합

import sys
sys.stdin = open("23886.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # 노드 개수, 리프 개수, 노드 번호

    tree = [0] * (N + 1)  # 순회할거 아니면 굳이 트리 dic 으로 X

    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    for i in range(N, 0, -1):  # 역순으로 부모노드 계산
        if i//2 > 0:  # 자식의 반이 부모, 1만 제외 (부모 없음)
            tree[i//2] += tree[i]

    print(f'#{tc} {tree[L]}')