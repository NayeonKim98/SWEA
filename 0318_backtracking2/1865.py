# 동철이의 일 분배

import sys
sys.stdin = open("1865.input.txt", "r")

def find_max_probability(n, cost_matrix):
    max_probability = 0
    visited = [False] * n

    def backtrack(product, total_probability):
        nonlocal max_probability

        if total_probability <= max_probability:
            return

        if product == n:
            max_probability = total_probability
            return

        for factory in range(n):
            if not visited[factory]:
                visited[factory] = True
                backtrack(product + 1, total_probability * cost_matrix[product][factory]/100)
                visited[factory] = False

    backtrack(0, 1)
    return max_probability

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cost_matrix = [list(map(int, input().split())) for _ in range(N)]

    result = find_max_probability(N, cost_matrix)
    print(f"#{t} {result * 100:.6f}")

# T = int(input())
#
#
# def dfs(idx, visited, value):
#     global result
#
#     if value <= result:
#         return
#
#     if idx == N:
#         result = max(result, value)
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             dfs(idx + 1, visited, value * float(matrix[idx][i]) / 100)
#             visited[i] = False
#
#
# for test_case in range(1, 1 + T):
#     N = int(input())
#     matrix = []
#     result = 0
#     for _ in range(N):
#         matrix.append(list(map(int, input().split())))
#     visited = [False] * N
#     dfs(0, visited, 1)
#     print(f'#{test_case} {round(result * 100, 6):.6f}')