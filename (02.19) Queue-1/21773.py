# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
from collections import deque
import sys
sys.stdin = open("21773.input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    remain_pizza = deque(map(int, input().split()))     # 치즈 개수 생성
    fire_pizza = deque()                                # 돌림 화덕 생성
    front = rear = 0

    for i in range(N):
        fire_pizza.append(remain_pizza.popleft())

    print(remain_pizza)
    print(fire_pizza)

    while fire_pizza[rear] == 0:                                   # 남은 피자가 없을 때 까지
        if fire_pizza[rear] == 0:
            fire_pizza.popleft()
            fire_pizza.append(remain_pizza[0])
        fire_pizza[rear] //= 2
        fire_pizza.append(fire_pizza.popleft())
        print(fire_pizza)

    print(f'#{tc} {fire_pizza[0]}')