# 정식이의 은행업무

import sys
sys.stdin = open("4366.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    binary = input()
    ternary = input()

    # 2진수에서 한 자리만 바꿔 가능한 10진수 값 저장
    binary_candidates = []
    for i in range(len(binary)):
        modified = list(binary)
        modified[i] = '1' if binary[i] == '0' else '0'  # 해당 자리 반전
        binary_candidates.append(int("".join(modified), 2))  # 10진수 변환 후 저장

    # 3진수에서 한 자리만 바꿔 가능한 10진수 값과 비교
    for i in range(len(ternary)):
        for digit in '012':  # 3진수에서 가능한 숫자들
            if ternary[i] != digit:  # 기존 값과 다르게 변경
                modified = list(ternary)
                modified[i] = digit
                decimal_value = int("".join(modified), 3)  # 10진수 변환

                if decimal_value in binary_candidates:  # 2진수 수정값과 일치 확인
                    print(f"#{tc} {decimal_value}")
                    break