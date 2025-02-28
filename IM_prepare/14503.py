# 로봇 청소기(14503,bj)

N, M = map(int, input().split())
sti, stj, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 반시계방향 90도 회전 = d = (d + 3) % 4

count = 0  # 청소한만큼 카운트할 것

arr[sti][stj] = 1
count += 1
ci, cj = sti, stj

while 0 <= ci < N and 0 <= cj < M:
    cd = d
    for k in range(5):
        d = (d + 3) % 4  # 반시계로 90도 회전
        ni, nj = ci + direction[d][0], cj + direction[d][1]

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:  # 회전했는데 거기 값이 0이면 청소하러 감.
            ci, cj = ni, nj
            arr[ci][cj] = 1
            count += 1
            continue  # 청소할 장소 찾았으면 for 문 더 돌 필요 없어서


    ni, nj = ci - direction[d][0], cj - direction[d][1]
    if cd == d and arr[ni][nj] == 1:  # 4 방향 다 탐색하고 나왔는데 1이면 후진할것임.
        ci, cj = ni, nj

print(count)


