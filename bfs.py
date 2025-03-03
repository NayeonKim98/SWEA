def bfs_traversal(V, E, edges):
    # 그래프 초기화
    graph = {i: [] for i in range(1, V + 1)}  # 1번부터 V번까지의 노드
    for i in range(0, len(edges), 2):
        frm, to = edges[i], edges[i + 1]
        graph[frm].append(to)
        graph[to].append(frm)  # 무방향 그래프

    # 숫자가 작은 노드부터 방문하도록 정렬
    for node in graph:
        graph[node].sort()  # 작은 숫자부터 방문해야 하므로 정렬

    # BFS 탐색을 위한 큐 및 방문 체크
    queue = [1]  # 시작 노드 1
    top = 0  # 큐의 맨 앞을 가리키는 인덱스
    visited = [False] * (V + 1)
    visited[1] = True  # 시작 노드 방문 체크

    while top < len(queue):  # 큐가 빌 때까지 반복
        node = queue[top]  # 현재 탐색할 노드
        top += 1  # pop(0) 대신 top 증가

        # 인접 노드 탐색 (숫자가 작은 것부터 방문)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)  # BFS에서는 큐에 추가

    # 탐색 경로를 '1-2-3-4-5-7-6' 형식으로 반환
    return '-'.join(map(str, queue))

# 테스트 데이터
T = 1
test_cases = [
    (7, 8, [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7])
]

# 테스트 실행
for i, (V, E, edges) in enumerate(test_cases, 1):
    result = bfs_traversal(V, E, edges)
    print(f"#{i} {result}")
