# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 (완전탐색)

import sys
sys.stdin = open("23895.input.txt", "r")

def recur(cnt, total):
    global min_sum

    if total >= min_sum:  # total 더하다보니 min 보다 크다하면 그냥 return
        return

    if cnt == N - 1:
        total += arr[path[-1] - 1][0]  # N만큼 찍고 return 하기 전에 마지막으로 total 추가
        min_sum = min(min_sum, total)  # 총 합을 비교
        return

    for num in range(2, N + 1):
        if used[num] == 1:
            continue

        used[num] = 1
        path.append(num)
        recur(cnt + 1, total + arr[path[-2] - 1][num - 1])  # 그 전 total 에 arr[path[-2] - 1][num - 1] 추가
        path.pop()
        used[num] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * (N + 1)
    min_sum = float('inf')
    path = [1]

    recur(0, 0)
    print(f'#{tc} {min_sum}')