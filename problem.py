def subset_sum(S, target, index=0, current=[]):
    # 현재 부분집합의 합이 target이면 출력
    if sum(current) == target:
        print(current)
        return

    # 종료 조건: 인덱스가 배열 끝을 넘어가면 종료
    if index >= len(S):
        return

    # 현재 원소 포함하는 경우
    subset_sum(S, target, index + 1, current + [S[index]])

    # 현재 원소 포함하지 않는 경우
    subset_sum(S, target, index + 1, current)

# 실행
S = [3, 1, 2, 5]
target = 5
subset_sum(S, target)
