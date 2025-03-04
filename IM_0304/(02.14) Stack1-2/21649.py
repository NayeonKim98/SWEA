# Stack I. 연습문제 3. 그래프 탐색 (가장 먼저 풀어보기)

import sys
sys.stdin = open("21649.input.txt", "r")

def dfs(v, n):  # v = 시작 정점, n = 총 정점 개수
    result = []
    visited = [0] * (n + 1)
    stack = [0] * (n + 1)
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

                v = w  # 정점을 인접정점인 w로 바꾸기

                break

        else:  # 방문 했던 정점이면,
            if top != 0:  # 지금 top 에 뭔가 있다면
                top -= 1  # 한 칸 전으로 가서
                v = stack[top]  # 다시 탐색

                if v == 0:  # 거꾸로 오면서 정점이 0에 왔다면, break
                    break
    return result
T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점 개수, 간선 개수 확인
    spots = list(map(int, input().split()))

    adj_list = [[] for _ in range(V + 1)]

    for i in range(E):
        v, w = spots[i * 2], spots[i * 2 + 1]   # 현재 정점, 인접 정점
        adj_list[v].append(w)
        adj_list[w].append(v)

    answer = dfs(1, V)
    print(f'#{tc}', '-'.join([str(num) for num in answer]))