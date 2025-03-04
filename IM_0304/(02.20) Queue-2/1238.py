import sys
sys.stdin = open(r"C:\Users\twony\Desktop\SWEA\(02.20) Queue-2\1238.input.txt", "r", encoding="utf-8")

T = 10
for tc in range(1, 11):
    N, S = map(int, input().split())  # 데이터 수와 시작점
    arr = list(map(int, input().split()))
    
    adj_lst = [[] for _ in range(101)]
    visited = [0] * 101

    # 인접 리스트 생성
    for i in range(N // 2):
        v, w = arr[2 * i], arr[2 * i + 1]
        adj_lst[v].append(w)

    stack = []
    stack.append(S)
    visited[S] = 1

    while stack:
        next_stack = []
        
        for v in stack:
            for adj_node in adj_lst[v]:
                if not visited[adj_node]:
                    next_stack.append(adj_node)
                    visited[adj_node] = 1
                    max_num = max(next_stack)

        stack = next_stack
        
    print(f'#{tc} {max_num}')