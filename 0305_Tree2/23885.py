# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

import sys
sys.stdin = open("23885.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))

    heap = [0]  # 최소 힙 배열 (0번째 인덱스는 필요없으니까 이 뒤로 추가할 예정)

    for num in tree:  # 1~N번째 숫자까지 돌면서 전부 부모 찾기 (1 제외)
        heap.append(num)
        idx = len(heap) - 1

        while idx > 1 and heap[idx] < heap[idx//2]:
            heap[idx], heap[idx//2] = heap[idx//2], heap[idx]  # 부모와 자식 자리 바꾸기
            idx //= 2  # 부모로 이동

    last_idx = len(heap) - 1

    total_sum = 0
    while last_idx > 1:  # 1(루트) 되기 전까지
        last_idx //= 2
        total_sum += heap[last_idx]

    print(f'#{tc} {total_sum}')
