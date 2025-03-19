# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

import sys
sys.stdin = open("22005.input.txt", "r")

# 조장 번호 찾기
def find(parent, x):
    if parent[x] != x:  # 대표 아니면 다시 찾기.
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

# a조와 b조를 합치기
def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a  # b의 대표를 a의 대표로 변경

def count_groups(n, pairs):
    """조 개수를 세는 함수"""
    parent = list(range(n + 1))  # 자기 자신이 초기 대표

    for a, b in pairs:  # 받은 쌍을 하나의 그룹으로 합치기
        union(parent, a, b)

    # 모든 노드의 부모 개수를 통해 조 개수를 찾기
    groups = set(find(parent, i) for i in range(1, n + 1))
    return len(groups)

t = int(input().strip())
for tc in range(1, t + 1):
    n, m = map(int, input().split())  # 학생 수, 신청서 수
    data = list(map(int, input().split()))  # 조 신청서 리스트

    pairs = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]

    result = count_groups(n, pairs)
    print(f"#{tc} {result}")
