def dfs_stack(graph, start):
    stack = [start]  # 스택에 시작 노드 삽입
    visited = []  # 방문한 노드 저장

    while stack:
        node = stack.pop()  # 스택의 최상단 노드 꺼냄
        visited.append(node)  # 방문 순서 기록

        # 현재 노드의 자식들을 스택에 push (오름차순 정렬된 상태여야 원하는 순서대로 방문 가능)
        for neighbor in sorted(graph[node], reverse=True):
            stack.append(neighbor)

        # 현재 스택 상태 출력
        print(f"스택: {stack}")

    return visited


# 그래프 정의 (트리 구조)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [7],
    6: [],
    7: []
}

# DFS 실행
result = dfs_stack(graph, 1)
print("DFS 방문 순서:", result)
