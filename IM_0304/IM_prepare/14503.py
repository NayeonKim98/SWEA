N, M = map(int, input().split())
sti, stj, d = map(int, input().split())  # 시작점과 처음 방향
arr = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 반시계방향 회전: (d + 3) % 4

# 청소한 영역 카운트
def clean_room():
    global d, arr
    count = 1  # 시작 지점 청소
    arr[sti][stj] = 2  # 청소된 위치는 2로 표시
    ci, cj = sti, stj
    
    while True:
        cleaned = False
        for _ in range(4):  # 네 방향 탐색
            d = (d + 3) % 4  # 반시계 방향 회전
            ni, nj = ci + direction[d][0], cj + direction[d][1]
            
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:  # 청소되지 않은 빈칸 발견
                ci, cj = ni, nj
                arr[ci][cj] = 2  # 청소 표시
                count += 1
                cleaned = True
                break
        
        if not cleaned:  # 네 방향 모두 청소할 곳이 없을 때
            back_i, back_j = ci - direction[d][0], cj - direction[d][1]
            if 0 <= back_i < N and 0 <= back_j < M and arr[back_i][back_j] != 1:  # 벽이 아니면 후진
                ci, cj = back_i, back_j
            else:
                break  # 후진할 수 없으면 작동 종료
    
    return count

print(clean_room())