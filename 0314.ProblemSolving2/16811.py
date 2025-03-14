# 당근 포장하기

import sys
sys.stdin = open("16811.input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    max_weight = max(carrots)

    weights = [0] * (max_weight + 1)
    answer = -1

    # weight counting
    for i in range(N):
        weights[carrots[i]] += 1

    # two pointer 로 풀이. i는 medium 시작점, j는 big 시작점
    for i in range(2, max_weight):
        for j in range(i + 1, max_weight + 1):
            small = sum(weights[1:i])
            medium = sum(weights[i:j])
            big = sum(weights[j:])

            if max(small, medium, big) > N // 2:
                continue

            result = max(abs(small - medium), abs(medium - big), abs(big - small))
            answer = result if answer == -1 else min(result, answer)

    print(f'#{tc} {answer}')