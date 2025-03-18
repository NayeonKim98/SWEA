# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용

import sys
sys.stdin = open("23898.input.txt", "r")


def find_min_cost(n, cost_matrix):
    min_cost = float('inf')
    visited = [False] * n  # 공장 방문 여부

    def backtrack(product, total_cost):
        nonlocal min_cost

        # 가지치기: 현재 비용이 최소 비용보다 크면 중단
        if total_cost >= min_cost:
            return

        # 모든 제품을 배정한 경우 최소 비용 갱신
        if product == n:
            min_cost = total_cost
            return

        # 각 공장에 제품 배정
        for factory in range(n):
            if not visited[factory]:  # 공장이 사용되지 않았다면
                visited[factory] = True
                backtrack(product + 1, total_cost + cost_matrix[product][factory])
                visited[factory] = False  # 백트래킹

    backtrack(0, 0)
    return min_cost


# 입력 받기
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cost_matrix = [list(map(int, input().split())) for _ in range(N)]

    result = find_min_cost(N, cost_matrix)
    print(f"#{t} {result}")