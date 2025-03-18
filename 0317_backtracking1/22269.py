# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

import sys
sys.stdin = open("22269.input.txt", "r")

def quick_sort(arr):
    if len(arr) <= 1:  # 길이가 1 이하면 정렬 필요 없음.
        return arr
    pivot = arr[len(arr) // 2]  # 중간 값을 피벗으로 선택
    left = [x for x in arr if x < pivot]
    middle = [ x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = quick_sort(arr)

    print(f'#{tc} {sorted_arr[N // 2]}')

