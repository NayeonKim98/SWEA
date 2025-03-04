# [S/W 문제해결 기본] 4일차 - 길찾기

import sys
sys.stdin = open("1219.input.txt", "r")

def dfs(v, n):  # v는 현재 정점, n은 정점 개수
    result = []
    visited = [0]*100
    stack = [0]*100
    top = 0

    while True:
        if not visited[v]:
            visited[v] = 1
            result.append(v)

        for w in adj_list[v]:
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

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]

    for i in range(E):
        v, w = arr[i * 2], arr[i * 2 + 1]
        adj_list[v].append(w)

    result = dfs(0, V)

    if 99 in result:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')