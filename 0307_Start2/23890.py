# Start 연습문제 3. 16진수 암호비트패턴 출력하기

import sys
sys.stdin = open("23890.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    hex_str = input().strip()

    hex_to_bin_map = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }

    code_pattern = {
        '001101': "0", '010011': "1", '111011': "2", '110001': "3",
        '100011': "4", '110111': "5", '001011': "6", '111101': "7",
        '011001': "8", '101111': "9"
    }

    # 16진수를 2진수로 변환
    binary_str = ''
    for hex_num in hex_str:
        binary_str += hex_to_bin_map[hex_num]


    # 코드 해석
    i = 0
    code_lst = []
    while i <= (len(binary_str) - 6):
        bin_to_solve = binary_str[i:i+6]
        if bin_to_solve in code_pattern:  # 만약 코드패턴 안에 있는 2진수라면
            code_lst.append(code_pattern[bin_to_solve])
            i += 5  # 만약 코드패턴에 있음 6칸 뛰어야해서
        i += 1

    result = ' '.join(map(str, code_lst))
    print(f'#{tc} {result}')