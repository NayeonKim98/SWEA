# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

import sys
sys.stdin = open("21647.input.txt", "r")

def dp(N):
    dp = [0] * (N + 1)
    dp[10] = 1
    dp[20] = 3

    for i in range(30, N + 1, 10):
        dp[i] = dp[i - 10] + 2 * dp[i - 20]

    return dp[N]

T = int(input())
for tc in range(1, T+1):
     N = int(input())

     result = dp(N)
     print(f'#{tc} {result}')