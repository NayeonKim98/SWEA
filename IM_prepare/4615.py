# 재미있는 오셀로 게임

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\SWEA\IM_prepare\4615.input.txt", "r", encoding="utf-8")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    direction = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]

    # 초기 설정 (가운데에 돌 놓기)
    arr[N//2 - 1][N//2 - 1] = 2
    arr[N//2 - 1][N//2] = 1
    arr[N//2][N//2 - 1] = 1
    arr[N//2][N//2] = 2

    # 순서에 맞춰 하나씩 돌 놓기
    for _ in range(M):
        i, j, color = map(int, input().split())
        arr[i-1][j-1] = color
        
        # 자신과 같은 색의 돌을 발견하면, 그 전 다른색 담아놨다 그 사이 애들 색 바꿈.
        for di, dj in direction:
            stack = []
            for k in range(N):
                ni, nj = (i-1) + di * (k + 1), (j-1) + dj * (k + 1)
                if not (0 <= ni < N and 0 <= nj < N):
                    break
                if arr[ni][nj] == 0:
                    break
                elif arr[ni][nj] == 3 - color:  # 다른 색이면, 스택에 추가
                    stack.append([ni, nj])
                elif arr[ni][nj] == color:  # 같은 색이면, 싹 변환
                    while stack:
                        ni, nj = stack.pop()
                        arr[ni][nj] = color
                    break

    count_black = sum(row.count(1) for row in arr)
    count_white = sum(row.count(2) for row in arr)          
    
    print(f'#{tc} {count_black} {count_white}')