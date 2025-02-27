# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
from collections import deque

import sys
sys.stdin = open("21812.input.txt", "r")

def bfs(s, g, adj_node):
    visited = [-1] * (V + 1)
    q = deque()
    q.append(s)
    visited[s] = 0

    while q:
        cur_pos = q.popleft()

        if cur_pos == g:
            return visited[g]

        for next_pos in adj_node[cur_pos]:
            if visited[next_pos] == -1:
                q.append(next_pos)
                visited[next_pos] = visited[cur_pos] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # V = 노드 개수, E = 간선 정보 개수
    arr = [list(map(int, input().split())) for _ in range(E)]   # E개의 간선 연결 노드 정보
    S, G = map(int, input().split())    # 출발 번호 S 와 도착번호 G

    adj_node = [[] for _ in range(V + 1)]

    for v, w in arr:
        adj_node[v].append(w)
        adj_node[w].append(v)

    result= bfs(S, G, adj_node)
    print(f'#{tc} {result}')
