# [S/W 문제해결 기본] 7일차 - 미로1
from collections import deque

import sys
sys.stdin = open("1226.input.txt", "r")

T = 10
for tc in range(1,11):
    test_case = int(input())
    maze = list(list(map(int, input())) for _ in range(10))

    print(f'#{test_case} {maze}')