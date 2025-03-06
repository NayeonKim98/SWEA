# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

import sys
sys.stdin = open("1240.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code = [list(map(int, input())) for _ in range(N)]

    # 1이 들어있는 행 찾기
    for i in range(N):
        for j in range(M):
            if code[i][j] == 1:
                stline = i
                break

    binary_code = ''
    binary_code += "".join(map(str, code[stline])).rstrip('0')  # 리스트를 문자로 바꿈(코드 1로 끝나니까 오른쪽 0 제거)
    binary_code = binary_code[len(binary_code)-56:]  # 길이 56의 암호코드

    decimal_dir = {
        '0001101': "0", '0011001': "1", '0010011': "2", '0111101': "3",
        '0100011': "4", '0110001': "5", '0101111': "6", '0111011': "7",
        '0110111': "8", '0001011': "9"
    }

    # 문자열을 7개씩 잘라서 10진수로 변환
    decimal_lst = []
    i = 0
    while i < len(binary_code):  # 문자열의 마지막에 다다를 때까지 반복
        code_to_solve = binary_code[i:i+7]
        decimal_lst.append(decimal_dir[code_to_solve])
        i += 7

    decimal_code = list(map(int, decimal_lst))

    # 홀수자리, 짝수자리 구분해서 합 구하기
    even_sum = 0
    odd_sum = 0
    for i, num in enumerate(decimal_code):
        if (i+1) % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    # 결과 도출
    if (3 * odd_sum + even_sum) % 10 == 0:
        result = sum(decimal_code)
    else:
        result = 0

    print(f'#{tc} {result}')

