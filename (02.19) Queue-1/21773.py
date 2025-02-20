# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

from collections import deque

import sys
sys.stdin = open("21773.input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    cheese = list(map(int, input().split()))    # 치즈 개수 생성
    non_cooked_pizza = deque()                  # 대기 피자 생성
    cooked_pizza = deque()                      # 화덕에 들어간 피자 생성
    wait_pizza = deque()

    for i in range(M):
        non_cooked_pizza.append([i+1, cheese[i]])

    for i in range(N):
        cooked_pizza.append([i+1, cheese[i]])
        non_cooked_pizza.popleft()

    # 여기부터 화덕 피자 돌리기 시작.
    # 화덕에 넣을 때, 첫 번째 자리에 넣어야함.
    while len(cooked_pizza) > 1:                # 마지막 피자가 남을 때까지

        if cooked_pizza[0][1] == 0:  # 치즈가 다 녹으면
            cooked_pizza.popleft() # 꺼내고
            if non_cooked_pizza:  # 아직 굽지 않은 피자가 남아있으면
                wait_pizza = cooked_pizza   # 대기 피자에 화덕 피자들 넣어뒀다가
                cooked_pizza = deque()
                cooked_pizza.append(non_cooked_pizza.popleft())     # 새로 들어올 피자를 넣고
                for pizza in wait_pizza:
                    cooked_pizza.append(pizza)      # 원래 대기 피자에 있던 애들도 대려옴.

        cooked_pizza[0][1] //= 2
        cooked_pizza.append(cooked_pizza.popleft())  # 치즈가 다 녹지 않아도 돌려야함

    print(f'#{tc} {cooked_pizza[0][0]}')

# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
#
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
#
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
#
# if cooked_pizza[0][1] == 0:
#     cooked_pizza.popleft()
#     cooked_pizza.append(non_cooked_pizza.popleft())
#
# if cooked_pizza[0][1] == 0:
#     cooked_pizza.popleft()
#       # 빈 리스트에 cooked_pizza를 통째로 가져다 대기시켜놓고
#     cooked_pizza.append(non_cooked_pizza.popleft())
        # 이러고 나서 다시 넣는다.
#
# if cooked_pizza[0][1] == 0:
#     cooked_pizza.popleft()
#     # cooked_pizza.append(non_cooked_pizza.popleft())
#
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
#
# cooked_pizza[0][1] //= 2
# cooked_pizza.append(cooked_pizza.popleft())
# cooked_pizza[0][1] //= 2
# if cooked_pizza[0][1] == 0:
#     cooked_pizza.popleft()
#     # cooked_pizza.append(non_cooked_pizza.popleft())