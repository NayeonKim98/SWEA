# 국민셔플

import sys
sys.stdin = open("20349.input.txt", "r")


# 오버핸드 셔플
def overhand_shuffle(deck, N):
    part = int(N * 0.37)
    top_part = deck[:N - part]
    bottom_part = deck[N - part:]

    return bottom_part + top_part

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
    N, T = map(int, input().split())
    deck = list(range(1, N + 1))

    # 셔플을 repeat_T번 반복
    for _ in range(T):
        deck = overhand_shuffle(deck, N)
        deck = perfect_shuffle(deck, N)

    print(f'#{tc}', *deck)