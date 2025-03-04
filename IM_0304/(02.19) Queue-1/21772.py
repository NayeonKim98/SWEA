# 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전

import sys
sys.stdin = open("21772.input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())            # 전체 길이 N과 이동 횟수 M
    queue = list(map(int, input().split()))     # N 만큼의 que list

    front = M % N

    print(f'#{tc} {queue[front]}')