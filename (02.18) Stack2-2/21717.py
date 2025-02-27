# 줄 서는 방법 - 순열 문제

import math


def solution(n, k):
    numbers = list(range(1, n + 1))  # 1부터 n까지 숫자 리스트
    answer = []
    k -= 1  # 0-based index로 변환

    while n > 0:
        n -= 1
        fact = math.factorial(n)  # (n-1)! 계산
        index = k // fact  # 현재 자리 숫자의 인덱스
        answer.append(numbers.pop(index))  # 숫자를 선택하고 제거
        k %= fact  # 다음 자리 계산을 위해 k 값 갱신

    return answer