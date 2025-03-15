 # 이진수

import sys
sys.stdin = open("13016.input.txt", "r")

def hex_to_binary(hex_str):
    hex_to_bin_map = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }

    binary_str = "".join(hex_to_bin_map[digit] for digit in hex_str)
    return binary_str

T = int(input())
for tc in range(1, T + 1):
    N, hex_str = map(str, input().split())

    result = hex_to_binary(hex_str)
    print(f'#{tc} {result}')