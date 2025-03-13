# 당근 포장하기

import sys
sys.stdin = open("16811.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    carrots.sort()

    max_size = N//2  # 한 상자에 들어갈 최대 개수

    min_diff = float('inf')
    found = False

    for i in range(1, N - 1):
        for j in range(i + 1, N):  # 이렇게 저렇게 나눠보면서 조건 부합하는 경우 찾기
            small = carrots[:i]
            medium = carrots[i:j]
            large = carrots[j:]

            if not small or not medium or not large:  # 빈 상자가 있는지 확인
                continue

            if len(small) > max_size or len(medium) > max_size or len(large) > max_size:  # max_size 를 안넘는지 확인
                continue

            diff = max(len(small), len(medium), len(large)) - min(len(small), len(medium), len(large))
            min_diff = min(min_diff, diff)
            found = True

    if found:
        print(f'#{tc} {min_diff}')
    else:
        print(f'#{tc} -1')