# 이진수2

import sys
sys.stdin = open("13017.input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = input()

    binary_lst = []
    a = int(0.5 * (10 ** (len(N) - 2)))  # 주어진 수의 소숫점 자리만큼 나눌 수의 자릿수를 바꿈
    N = int(N[2:])
    while len(binary_lst) < 13:  # 13자리 넘어가면 overflow
        binary_lst.append(int(N // a))  # N을 나누는 수로 나눴을 때의 몫을 이진수로 저장
        N %= a  # N을 나머지로 계속 갱신
        a /= 2  # 나누는 수는 계속 반으로 나눠 갱신
        if N == 0:  # 만약 나눠야하는 수가 0이면 종료
            break

    result = ''.join(map(str, binary_lst))

    if len(binary_lst) == 13:
        result = 'overflow'

    print(f'#{tc} {result}')