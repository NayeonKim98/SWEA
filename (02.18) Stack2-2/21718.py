# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

import sys
sys.stdin = open("21718.input.txt", "r")

def backtrack(N, arr, row, current_sum, visited, min_sum):
    if row == N: # 모든 행을 처리한 경우 (재귀 종료 조건)
        return min(min_sum, current_sum) # 최소 합 갱신 후 반환

    for col in range(N): # 현재 행의 모든 열을 순회
        if not visited[col]: # 해당 열이 아직 선택되지 않은 경우
            visited[col] = 1 # 해당 열을 선택
            min_sum = backtrack(N, arr, row + 1, current_sum + arr[row][col], visited, min_sum) # 다음 행으로 재귀 호출
            visited[col] = 0 # 해당 열 선택 해제 (백트래킹)

    return min_sum # 최소 합 반환

T = int(input()) # 테스트 케이스 개수 입력
for tc in range(1, T + 1): # 각 테스트 케이스에 대해 반복
    N = int(input()) # 배열 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)] # 배열 입력

    visited = [0] * N # 열 방문 여부 초기화
    min_sum = backtrack(N, arr, 0, 0, visited, float('inf')) # 백트래킹 시작
    print(f'#{tc} {min_sum}') # 결과 출력


# def backtrack(N, arr):
#     visited = [0] * N
#     total = 0
#     min_total = float('inf')
#     i = 0
#     j = 0
#
#     while i <= N-1:
#         for j in range(N):
#             if not visited[j]:
#                 total += arr[i][j]
#                 i += 1
#                 visited[j] = 1
#         min_total = min(total, min_total)
#
#     return min_total
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     result = backtrack(N, arr)
#     print(f'#{tc} {result}')