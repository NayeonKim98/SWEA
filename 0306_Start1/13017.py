# 이진수2

import sys
sys.stdin = open("13017.input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = float(input())  # 문자열 대신 float로 변환
    binary_lst = ""

    while N > 0:
        if len(binary_lst) >= 12:  # 12자리 초과하면 overflow
            binary_lst = "overflow"
            break

        N *= 2
        if N >= 1:
            binary_lst += "1"
            N -= 1
        else:
            binary_lst += "0"

    print(f"#{tc} {binary_lst}")
