# Stack I. 연습문제 3. 그래프 탐색 (가장 먼저 풀어보기)

import sys

sys.stdin = open("21649.input.txt", "r")


# 함수 만들기
def dfs(v, n):
    """
    v : 시작정점
    n : 총 정점 개수
    """
    # 리턴용 리스트
    result = []
    # 방문확인용 리스트
    visited = [0] * (n + 1)
    # 스택
    stack = [0] * (n + 1)
    top = 0
    # 반복문을 통해 모든 그래프를 탐색할 수 있도록 한다.
    while True:
        # 방문하지 않은 정점이라면
        if not visited[v]:
            # 상태 변경해주기
            visited[v] = 1
            result.append(v)

        # 인접 정점으로 들어가기
        for w in adj_list[v]:
            # 방문하지 않았다면
            if not visited[w]:
                result.append(w)
                # 상태 변경
                visited[w] = 1
                # 스택에 넣어주기
                top += 1
                stack[top] = w
                # 현재 정점을 바꿔주기
                v = w
                # 바꾼 정점에서 다시 시작한다.
                break
            # 이미 방문했던 곳이라면 조용히 건너가면 된다.
        else:
            # 스택에 뭔가가 있다면
            if top != 0:
                # top 위치 하나 아래로
                top -= 1
                # 현재 정점도 바꿔주기
                v = stack[top]

                if v == 0:
                    break
    return result


# 테스트 케이스는 한번이다.
# 1. 정점 개수, 간선 개수 확인하기
V, E = map(int, input().split())
# 연결 정점들
spots = list(map(int, input().split()))

# 인접리스트 만들어서 인접 관계 저장하기
adj_list = [[] for _ in range(V + 1)]

for i in range(E):
    # 현재 정점, 인접 정점
    v, w = spots[i * 2], spots[i * 2 + 1]
    # 인접리스트에 넣기 -> 인덱스 활용
    adj_list[v].append(w)
    adj_list[w].append(v)

answer = dfs(1, V)
print('#1', '-'.join([str(num) for num in answer]))