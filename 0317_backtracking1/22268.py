# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬

import sys
sys.stdin = open("22268.input.txt", "r")

def merge_sort(arr, start, end):
    global count

    if end - start <= 1:  # 길이가 1 이하면 종료
        return arr[start:end]

    mid = (start + end) // 2  # 중간 지점

    left = merge_sort(arr, start, mid)
    right = merge_sort(arr, mid, end)

    # 왼쪽 마지막 > 오른쪽 마지막 -> 카운트
    if left[-1] > right[-1]:
        count += 1

    # 병합 과정 (투 포인터)
    sorted_lst = []
    i = j = 0
    while i < len(left) and j < len(right):  # 작은 원소를 먼저 집어넣기
        if left[i] <= right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:  # 오른쪽 원소가 더 작으면,
            sorted_lst.append(right[j])
            j += 1

    sorted_lst.extend(left[i:])  # 비교하면서 다 담은 상황에서, 어떤 인덱스가 넘치면 더이상 비교 불가. 나머지 그냥 집어넣음
    sorted_lst.extend(right[j:])

    return sorted_lst

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0

    sorted_arr = merge_sort(arr, 0, N)

    print(f'#{tc} {sorted_arr[N // 2]} {count}')