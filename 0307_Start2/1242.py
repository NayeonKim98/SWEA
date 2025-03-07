# [S/W 문제해결 응용] 1일차 - 암호코드 스캔

import sys
sys.stdin = open("1242.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 배열 세로, M = 배열 가로
    hex_num = [input() for _ in range(N)]

    # 리스트를 문자열로 변환
    hex_str = ''
    for num in hex_num:
        hex_str += num

    hex_to_bin_map = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }

    decimal_dir = {
        '3211': "0", '2221': "1", '2122': "2", '1411': "3",
        '1132': "4", '1231': "5", '1114': "6", '1312': "7",
        '1213': "8", '3112': "9"
    }

    # 16진수를 2진수로 변환
    binary_str = ''
    for hex_num in hex_str:
        binary_str += hex_to_bin_map[hex_num]

    # 2진수의 암호 해석 (7자리 숫자 + 1자리 검증코드)


    # 8개씩 숫자 끊어서 그 안에서 7자리 암호 확인.
    i = 0
    code = []
    while i < len(binary_str):
        ratio = ''
        bin_to_solve = binary_str[i:i+7]
        if bin_to_solve.count('1') >= 3:  # 1의 개수가 3개 이상일 때만 비율 탐색
            for i, num in enumerate(bin_to_solve):  # 비율 구하기
                if num == '1' and bin_to_solve[i + 1] == '0':
                    first_0_cnt = bin_to_solve[:i + 1].count('0')
                    first_1_cnt = bin_to_solve[:i + 1].count('1')
                    second_0_cnt = bin_to_solve[i + 1:].count('0')
                    second_1_cnt = bin_to_solve[i + 1:].count('1')
                    break
            ratio += str(first_0_cnt)
            ratio += str(first_1_cnt)
            ratio += str(second_0_cnt)
            ratio += str(second_1_cnt)

            if ratio in decimal_dir:
                code.append(decimal_dir[ratio])
                i += 7
        i += 1

    print(code)