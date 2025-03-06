# Start 연습문제 1. 2진수를 10진수로 출력하기 (가장 먼저 풀기)

import sys
sys.stdin = open("23888.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N = 주어진 입력의 줄 개수
    binary_lst = [list(map(int, input().strip())) for _ in range(N)]  # 이진수가 줄 별로 들어있는 2차원 리스트

    binary_str = ''
    for i in range(N):
        binary_str += "".join(map(str, binary_lst[i]))  # 리스트를 문자로 바꿈

    decimal_lst = []
    i = 0
    while i < len(binary_str):  # 문자열의 마지막에 다다를 때까지 반복
        decimal_num = 0
        power = 0
        for digit in list(reversed(binary_str[i:i + 7])):  # 7개씩 묶어진 문자열을 10진수로 변환
            if digit == '1':  # 문자열이니까 1이 아니라 '1'
                decimal_num += 2 ** power
            power += 1
        decimal_lst.append(decimal_num)
        i += 7

    result = ' '.join(map(str, decimal_lst))
    print(f'#{tc} {result}')
