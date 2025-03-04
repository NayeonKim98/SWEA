# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

import sys
sys.stdin = open("21719.input.txt", "r")

def winner(a,b):
    if a[1] == b[1]:
        return a
    elif (a[1] == 1 and b[1] == 3) or (a[1] == 2 and b[1] == 1) or (a[1] == 3 and b[1] == 2):
        return a
    else:
        return b

def tournament(cards):
    if len(cards) == 1:
        return cards[0]
    mid = len(cards) // 2
    left_winner = tournament(cards[:mid])
    right_winner = tournament(cards[mid:])
    return winner(left_winner, right_winner)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_list = list(map(int, input().split()))
    card_idx = [[i+1, card_list[i]] for i in range(N)]
    result = tournament(card_idx)
    print(f'#{tc} {result[0]}')

