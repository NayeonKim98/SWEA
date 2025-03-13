# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 (그리디 알고리즘)

import sys
sys.stdin = open("23896.input.txt", "r")

def check_win(cards):
    count = [0] * 10

    for card in cards:
        count[card] += 1  # 각 숫자의 개수 카운트

    # triplet 확인 (같은 숫자 3개)
    for i in range(10):
        if count[i] >= 3:
            return True

    # run 확인 (연속 숫자 3개)
    for i in range(8):  # 8, 9 에서 시작 시 연속 3개의 카드를 만들 수 없음.
        if count[i] >= 1 and count[i + 1] >= 1 and count[i + 2] >= 1:
            return True
    return False

# 재귀를 사용해 카드가 하나씩 추가될 때마다 승자가 있는지 확인
def dfs(cards, idx, p1, p2):
    if len(p1) >= 3 and check_win(p1):
        return 1
    if len(p2) >= 3 and check_win(p2):
        return 2

    if idx == 12:
        return 0

    if idx % 2 == 0:
        result = dfs(cards, idx + 1, p1 + [cards[idx]], p2)
    else:
        result = dfs(cards, idx + 1, p1, p2 + [cards[idx]])

    return result

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    result = dfs(cards, 0, [], [])
    print(f'#{tc} {result}')