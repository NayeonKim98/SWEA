# 파스칼의 삼각형

import sys
sys.stdin = open("2005.input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1]*_ for _ in range(1, N+1)]

    for i in range(1, N-1): # 행은 두 번째 행부터 덧셈에 사용할 것임.
        for j in range(i):  # 열은 i가 1이면 0 (다음 행에 바꿀 숫자 1개) , i가 2면 0 1 (다음 행에 바꿀 숫자 2개) N과 관련 X
            arr[i+1][j+1] = arr[i][j] + arr[i][j+1]

    print(f'#{tc}')
    for nums in arr:
        print(" ".join(map(str,nums)))