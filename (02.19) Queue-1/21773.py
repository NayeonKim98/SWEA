# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

from collections import deque

import sys
sys.stdin = open(r"C:\Users\twony\Desktop\SWEA\(02.19) Queue-1\21773.input.txt", "r", encoding="utf-8")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))    # 치즈 개수 생성
    non_cooked_pizza = deque()                  # 대기 피자 생성
    cooked_pizza = deque()                      # 화덕에 들어간 피자 생성

    for i in range(M):
        non_cooked_pizza.append([i+1, cheese[i]])

    for i in range(N):
        cooked_pizza.append([i+1, cheese[i]])
        non_cooked_pizza.popleft()

    # 여기부터 화덕 피자 돌리기 시작.
    while len(cooked_pizza) > 1:  # 마지막 한 개 남을 때까지 반복
        pizza = cooked_pizza.popleft()  # 피자 꺼내기
        pizza[1] //= 2  # 치즈 녹이기

        if pizza[1] > 0:  # 치즈가 남아 있으면 다시 넣기
            cooked_pizza.append(pizza)
        else:  # 치즈가 다 녹았으면
            if non_cooked_pizza:  # 새로운 피자가 남아 있으면 추가
                cooked_pizza.append(non_cooked_pizza.popleft())

    print(f'#{tc} {cooked_pizza[0][0]}')