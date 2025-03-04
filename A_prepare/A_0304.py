# 나무에 물주기

def fixed_min_days_to_grow_trees(test_cases):
    """
    각 테스트 케이스마다 나무의 성장을 최소 일수 내에 목표 높이까지 도달하도록 계산하는 함수.
    """
    results = []
    index = 0

    T = test_cases[index]  # 테스트 케이스 개수
    index += 1

    for tc in range(1, T + 1):
        N = test_cases[index]  # 나무 개수
        index += 1
        tree_height = test_cases[index:index + N]  # 나무 높이 리스트
        index += N

        tree_height.sort()  # 오름차순 정렬 (최대 높이 찾기 용이)
        max_height = tree_height[-1]  # 가장 높은 나무의 높이
        water_day = [0] * N  # 각 나무가 자라야 할 일수를 저장할 리스트

        day = 0  # 총 걸리는 일수
        for i, tree in enumerate(tree_height):
            diff = max_height - tree  # 해당 나무가 자라야 할 높이 계산
            if diff == 0:
                continue  # 이미 최대 높이인 경우 넘어감
            elif diff % 2 == 0:
                water_day[i] = diff // 2  # 짝수 차이는 하루 2씩 자라는 패턴으로 해결 가능
                day += water_day[i] * 2
            else:
                water_day[i] = diff // 2 + 1  # 홀수 차이는 먼저 1을 더하고, 나머지를 2씩 증가
                day += water_day[i] * 1

        # 최대 물 주는 날이 짝수일 경우 하루 줄일 수 있는지 확인
        if day > 0 and max(water_day) % 2 == 0:
            results.append(f'#{tc} {day - 1}')
        else:
            results.append(f'#{tc} {day}')

    return results

# 내 원래 코드
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     tree_height = list(map(int, input().split()))
#     tree_height.sort()
#     max_height = tree_height[-1]
#     water_day = [0] * N
#
#     day = 0
#     for i, tree in enumerate(tree_height):
#         if (max_height - tree) % 2 == 0 and (max_height - tree) != 0:
#             water_day[i] = (max_height - tree) // 2
#             day += water_day[i] * 2
#         elif (max_height - tree) % 2 == 1:
#             water_day[i] = (max_height - tree) // 2 + 1
#             day += water_day[i] * 1
#         elif (max_height - tree) == 0:
#             water_day[i] == 0
#
#     if day > 0 and max(water_day) % 2 == 0:
#         print(f'#{tc} {day - 1}')
#     else:
#         print(f'#{tc} {day}')