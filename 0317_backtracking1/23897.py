# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

import sys
sys.stdin = open("23897.input.txt", "r")

def binary_search(target, sorted_list):
    left, right = 0, len(sorted_list) - 1
    last_direction = None  # left or right 로 초기화할 예정

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return True

        if sorted_list[mid] < target:  # target 이 더 오른쪽에 있으면 오른쪽 탐색
            if last_direction == "right":
                return False
            left = mid + 1
            last_direction = "right"

        elif sorted_list[mid] > target:  # target 이 더 왼쪽에 있으면 왼쪽 탐색
            if last_direction == "left":
                return False
            right = mid - 1
            last_direction = "left"

    return False

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))  # A는 정렬해서 사용
    B = list(map(int, input().split()))

    count = sum(binary_search(num, A) for num in B)

    print(f'#{tc} {count}')

