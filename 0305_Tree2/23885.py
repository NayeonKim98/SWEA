# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

import sys
sys.stdin = open("23885.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))

    heap = [0]  # 최소 힙 배열 (0번재 인덱스 필요 없으니 미리 추가한 것)

    for num in tree:
        heap.append(num)
        idx = len(heap) - 1

        while idx > 1 and heap[idx] < heap[idx//2]:  # 부모 전까지 이진 힙
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
            idx //= 2  # 부모로 이동

    last_idx = len(heap) - 1

    total_sum = 0
    while last_idx > 1:
        last_idx //= 2
        total_sum += heap[last_idx]

    print(f'#{tc} {total_sum}')