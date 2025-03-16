from collections import deque


def level_order_traversal(tree, root):
    queue = deque([root])  # BFS를 위한 큐 (탐색할 노드 저장)

    while queue:
        node = queue.popleft()  # 가장 앞에 있는 노드를 꺼냄
        print(node, end=" ")  # 방문한 노드 출력

        if node in tree:  # 현재 노드에 연결된 자식 노드가 있다면
            queue.extend(tree[node])  # 큐에 자식 노드들을 추가 (왼쪽 → 오른쪽 순)


# ✅ 예제 트리
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# 🏆 BFS 실행 (레벨 순서 순회)
level_order_traversal(tree, 'A')