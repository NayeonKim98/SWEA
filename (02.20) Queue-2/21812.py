# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
from collections import deque

import sys
sys.stdin = open("21812.input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V = 노드 개수, E = 간선 정보 개수
    arr = [list(map(int, input().split())) for _ in range(E)]   # E개의 간선 연결 노드 정보
    S, G = map(int, input().split())    # 출발 번호 S와 도착번호 G

    count = 0

    for i in range(E):
        if arr[i][0] == S:
            next = arr[i][1]
            count + = 1

    while arr[next][1] == G:
        for j in range(E):
            if next in arr[j]:
                count += 1
        ans = count

    print(f"#{tc} {ans}")

#1 [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
#2 [[1, 6], [2, 3], [2, 6], [3, 5]]
#3 [[2, 6], [4, 7], [5, 7], [1, 5], [2, 9], [3, 9], [4, 8], [5, 3], [7, 8]]

# # 1
# V = 6 E = 5
# arr = [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
# S = 1 G = 6
#
# # 2
# V = 7 E = 4
# arr = [[1, 6], [2, 3], [2, 6], [3, 5]]
# S = 1 G = 5
#
# # 4
# V = 9 E = 9
# arr = [[2, 6], [4, 7], [5, 7], [1, 5], [2, 9], [3, 9], [4, 8], [5, 3], [7, 8]]
# S = 1 G = 9
#
# # 1
# [1, 4] => [4, 6]
# count = 2
#
# # 2
# [1, 6] => [6, 2] => [2, 3]
# count = 4
#
# # 3
# [1, 5] => [5, 3] => [3, 9]
# count = 3
#
# ## 1
# for i in range(E):
#     if arr[i][0] == S:
#         next = arr[i][1]
#         count += 1
#
# for j in range(E):
#     if next in arr[j]:
#         next = arr[j][1]
#         count += 1
#
# if arr[next][1] == G:
#     result = count
#
# ## 2
# for i in range(E):
#     if arr[i][0] == S:
#         next = arr[i][1]
#         count += 1
#
# for j in range(E):
#     if next in arr[j]:
#         next = arr[j][1]
#         count += 1
#
# for j in range(E):
#     if next in arr[j]:
#         next = arr[j][1]
#         count += 1
#
# if arr[next][1] == G:
#     result = count
#
# arr = [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
#
# for i in range(5):
#     if 4 in arr[i]:
#         result = i
#
# print(result)   # 4