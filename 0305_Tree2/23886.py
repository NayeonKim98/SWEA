# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합

import sys
sys.stdin = open("23886.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)  # 순회할거 아니면 트리를 굳이 dic 으로 만들지 않아도 된다.

    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    for i in range(N, 0, -1):  # 역순으로 부모 노드를 계산
        if i//2 > 0:  # 자식의 반이 부모니까. 1은 부모 없으니까 제외.
            tree[i//2] += tree[i]  # 자식의 값만큼 더하기.

    print(f'#{tc} {tree[L]}')