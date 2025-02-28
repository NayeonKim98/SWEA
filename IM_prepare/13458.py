# 시험감독(13458, bj)

N = int(input())  # 시험장 개수
A = list(map(int, input().split()))  # 응시자 수
B, C = map(int, input().split())  # B = 한 시험장 응시자 수, C = 부감독 감시자 수

count = 0
for ai in A:
    total_supv = 0
    if ai % B != 0:
        total_supv = B * (ai//B + 1)
    elif ai % B == 0:
        total_supv = B * (ai//B)

    if C % total_supv != 0:
        count += total_supv//C + 1
    elif C % total_supv == 0:
        count += total_supv//C

print(count)
