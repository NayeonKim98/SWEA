def dfs_traversal(V, E, edges):
    # 그래프 초기화
    graph = {i: [] for i in range(1, V + 1)}  # 1번부터 V번까지의 노드
    for i in range(0, len(edges), 2):
        frm, to = edges[i], edges[i + 1]
        graph[frm].append(to)
        graph[to].append(frm)  # 무방향 그래프

    # 숫자가 작은 노드부터 방문하도록 정렬
    for node in graph:
        graph[node].sort()  # 작은 숫자가 앞에 오도록 정렬

    # DFS 탐색을 위한 스택 및 방문 체크
    stack = [1]  # 시작 노드 1
    visited = [False] * (V + 1)
    visited[1] = True  # 시작 노드 방문 체크
    path = []  # 탐색 경로 저장

    while stack:  # 스택이 빌 때까지 반복
        node = stack.pop()  # DFS는 후입선출이므로 pop() 사용
        path.append(node)  # 방문 순서 저장

        # 인접 노드 탐색 (숫자가 작은 것부터 방문해야 하므로 **거꾸로 넣기**)
        for neighbor in reversed(graph[node]):  # 작은 숫자가 먼저 탐색되려면 거꾸로 넣어야 함
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    # 탐색 경로를 '1-2-4-6-5-7-3' 형식으로 반환
    return '-'.join(map(str, path))

# 테스트 데이터
T = 1
test_cases = [
    (7, 8, [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7])
]

# 테스트 실행
for i, (V, E, edges) in enumerate(test_cases, 1):
    result = dfs_traversal(V, E, edges)
    print(f"#{i} {result}")
