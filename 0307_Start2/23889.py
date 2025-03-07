# Start 연습문제 2. 16진수를 10진수로 변환하기

import sys
sys.stdin = open("23889.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    hex_str = input()

    hex_to_bin_map = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }

    # 16진수를 2진수로 변환
    binary_str = ''
    for hex_num in hex_str:
        binary_str += hex_to_bin_map[hex_num]

    # 2진수를 10진수로 변환
    i = 0
    digit_lst = []
    while i < len(binary_str):
        binary_to_digit = binary_str[i:i+7]
        power = 0
        digit = 0
        for num in list(reversed(binary_to_digit)):
            if num == '1':
                digit += 2 ** power
            power += 1
        digit_lst.append(digit)
        i += 7

    # 10진수들 출력
    result = ' '.join(map(str, digit_lst))
    print(f'#{tc} {result}')