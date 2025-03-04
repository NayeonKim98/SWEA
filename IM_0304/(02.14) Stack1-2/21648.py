# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

import sys
sys.stdin = open("21648.input.txt", "r")


def dfs(v, N):  # v = 시작정점 N = 노드 개수
    result = []
    visited = [0] * (N + 1)
    stack = [0] * (N + 1)
    top = 0

    while True:
        if not visited[v]:
            visited[v] = 1
            result.append(v)

        for w in adj_arr[v]:
            if not visited[w]:
                visited[w] = 1
                result.append(w)
                top += 1
                stack[top] = w

                v = w

                break

        else:
            if top != 0:
                top -= 1
                v = stack[top]

                if v == 0:
                    break
    return result


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_arr = [[] for _ in range(V + 1)]

    for i in range(E):
        v, w = map(int, input().split())
        adj_arr[v].append(w)

    S, G = map(int, input().split())

    result = dfs(S, V)

    if G in result:
        answer = 1
    else:
        answer = 0
    print(f'#{tc} {answer}')