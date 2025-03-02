# 입력 받기
N = int(input())  # 시험장 개수
A = list(map(int, input().split()))  # 각 시험장의 응시자 수
B, C = map(int, input().split())  # 총감독관이 감시할 수 있는 수, 부감독관이 감시할 수 있는 수

total_supervisors = 0  # 필요한 감독관 수

for students in A:
    total_supervisors += 1
    students -= B

    if students > 0:  # 학생이 남아있으면
        total_supervisors += (students // C)
        if students % C != 0:  # 부감독이 봐주고 남는 학생 있으면,
            total_supervisors += 1

print(total_supervisors)