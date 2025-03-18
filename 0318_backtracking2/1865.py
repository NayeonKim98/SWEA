# 동철이의 일 분배

import sys
sys.stdin = open("1865.input.txt", "r")

def find_max_success_probability(worker_idx, assigned_tasks, current_prob):
    global max_probability

    # 만약 현재 확률이 기존 최댓값보다 낮다면 더 진행할 필요 없음 (가지치기)
    if current_prob <= max_probability:
        return

    # 모든 직원이 일을 배정받았을 때
    if worker_idx == num_workers:
        max_probability = max(max_probability, current_prob)
        return

    for task_idx in range(num_workers):  # 가능한 업무(task) 탐색
        if not assigned_tasks[task_idx]:  # 아직 할당되지 않은 업무인지 확인
            assigned_tasks[task_idx] = True  # 해당 업무를 현재 직원에게 배정
            new_prob = current_prob * (success_matrix[worker_idx][task_idx] / 100)  # 확률 계산

            find_max_success_probability(worker_idx + 1, assigned_tasks, new_prob)
            assigned_tasks[task_idx] = False  # 백트래킹 (다른 경우 탐색 위해 원상 복구)

T = int(input())
for test_case in range(1, T + 1):
    num_workers = int(input())
    success_matrix = [list(map(int, input().split())) for _ in range(num_workers)]

    max_probability = 0
    task_assigned = [False] * num_workers  # 각 업무가 배정되었는지 여부를 저장하는 리스트

    find_max_success_probability(0, task_assigned, 1)  # 첫 번째 직원부터 탐색 시작

    # 결과 출력 (소수점 6자리까지 출력)
    print(f'#{test_case} {round(max_probability * 100, 6):.6f}')


# def find_max_success_probability(assigned_tasks, worker_idx):
#     """
#     비트마스크 + 백트래킹을 활용한 최대 성공 확률 계산 함수
#     :param assigned_tasks: 현재까지 배정된 업무 (비트마스크)
#     :param worker_idx: 현재 처리 중인 직원 인덱스
#     :return: 현재까지의 최대 확률 값
#     """
#     if worker_idx == num_workers:  # 모든 직원에게 일을 할당 완료한 경우
#         return 1  # 곱셈 연산을 위해 1 반환
#
#     # 이미 해당 상태에서 계산된 최대 확률이 있다면 반환 (메모이제이션)
#     if memo[assigned_tasks] != -1:
#         return memo[assigned_tasks]
#
#     max_success_rate = 0  # 현재 상태에서의 최대 성공 확률 저장
#
#     for task_idx in range(num_workers):  # 각 업무(task) 탐색
#         if not (assigned_tasks & (1 << task_idx)):  # 아직 배정되지 않은 업무인지 확인
#             success_probability = success_matrix[worker_idx][task_idx] / 100  # 확률을 소수로 변환
#             if success_probability > 0:  # 확률이 0이면 탐색 불필요 (가지치기)
#                 new_assigned_tasks = assigned_tasks | (1 << task_idx)  # 현재 업무 배정 상태 저장
#                 max_success_rate = max(
#                     max_success_rate,
#                     success_probability * find_max_success_probability(new_assigned_tasks, worker_idx + 1)
#                 )
#
#     memo[assigned_tasks] = max_success_rate  # 현재 상태에서의 최대 성공 확률 저장 (메모이제이션)
#     return memo[assigned_tasks]
#
#
# # 🌟 입력 처리 및 실행
# T = int(input())  # 테스트 케이스 개수 입력
#
# for test_case in range(1, T + 1):
#     num_workers = int(input())  # 직원 및 업무 개수 입력
#     success_matrix = [list(map(int, input().split())) for _ in range(num_workers)]  # 확률 행렬 입력
#
#     memo = [-1] * (1 << num_workers)  # DP 테이블 초기화 (비트마스크 사용)
#
#     max_probability = find_max_success_probability(0, 0) * 100  # 첫 번째 직원부터 탐색 시작
#
#     print(f'#{test_case} {max_probability:.6f}')  # 소수점 6자리 출력
