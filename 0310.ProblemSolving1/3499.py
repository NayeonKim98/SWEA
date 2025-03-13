# 퍼펙트 셔플

import sys
sys.stdin = open("3499.input.txt", "r")

# 퍼펙트 셔플
def perfect_shuffle(deck, N):
    part = (N + 1) // 2  # 왼쪽 절반이 더 길도록 설정
    top_part = deck[:part]
    bottom_part = deck[part:]
    new_pf_deck = [0] * len(deck)

    for i in range(len(top_part)):
        new_pf_deck[2 * i] = top_part[i]

    for j in range(len(bottom_part)):
        new_pf_deck[2 * j + 1] = bottom_part[j]

    return new_pf_deck

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    deck = list(input().split())

    deck = perfect_shuffle(deck, N)
    print(f'#{tc}', *deck)