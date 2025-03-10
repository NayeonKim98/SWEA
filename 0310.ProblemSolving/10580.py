# 전봇대

import sys
sys.stdin = open("10580.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pole = [list(map(int, input().split())) for _ in range(N)]

    a_list = []
    b_list = []
    cnt = 0
    for ai, bi in pole:
        a_list.append(ai)
        b_list.append(bi)

    for i in range(N-1):
        if a_list[i] > a_list[i + 1]:
            cnt += 1
            a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
        if b_list[i] > b_list[i + 1]:
            cnt += 1
            b_list[i], b_list[i + 1] = b_list[i + 1], b_list[i]

    print(f'#{tc} {cnt}')