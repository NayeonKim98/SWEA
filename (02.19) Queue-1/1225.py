# [S/W 문제해결 기본] 7일차 - 암호생성기
from collections import deque

import sys
sys.stdin = open("1225.input.txt", "r")

T = 10
for _ in range(1, 11):
    tc = int(input())
    password = deque(map(int, input().split()))

    # 숫자를 순회하면서 1 2 3 4 5 6 감소
    # 그 숫자를 맨 뒤로 보냄.
    # 이 반복이 한 싸이클
    # -1 -2 -3 -4 -5 -6 감소 했는데 음수 => 0으로 유지 / 싸이클 종료 후 암호 생성
    # 8씩 더해지면서 감소

    while password[0] >= 0:
        j = 0
        while j < 5:
            j += 1
            if password[0]
            password[0] -= j
            password.append(password.popleft())

    print(f'#{tc} {password}')

