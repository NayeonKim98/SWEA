# [S/W 문제해결 기본] 7일차 - 암호생성기
from collections import deque

import sys
sys.stdin = open("1225.input.txt", "r")

T = 10
for _ in range(1, 11):
    tc = int(input())
    password = deque(map(int, input().split()))

    i = 0
    while password[0] > 0:
        for i in range(1, 6):
            password[0] -= i
            if password[0] <= 0:
                break
            password.append(password.popleft())

    password[0] = 0
    password.append(password.popleft())


    print(f'#{tc} {" ".join(map(str,list(password)))}')


