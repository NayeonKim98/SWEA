key_pad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]  # 0~9번까지의 키패드 위치
original_left_pos, original_right_pos = [3, 0], [3, 2]  # '*', '#'


def solution(numbers, hand):
    cur_left_pos, cur_right_pos = original_left_pos, original_right_pos  # 현재 위치를 저장
    result = []  # target 을 누르면 누른 손까락 저장

    for target in numbers:  # numbers 를 순회하며 목표 숫자를 저장
        target_pos = key_pad[target]  # 그 목표 숫자의 위치를 저장

        if target == 1 or target == 4 or target == 7:  # 왼손 사용
            cur_left_pos = target_pos
            result.append('L')

        elif target == 3 or target == 6 or target == 9:  # 오른손 사용
            cur_right_pos = target_pos
            result.append('R')

        elif target == 2 or target == 5 or target == 8 or target == 0:  # 둘 중 가까운 손, 거리가 같다면 손잡이에 따라 누르게 된다.
            left_target_dist = abs(cur_left_pos[0] - target_pos[0]) + abs(cur_left_pos[1] - target_pos[1])  # 왼손과 타겟의 거리
            right_target_dist = abs(cur_right_pos[0] - target_pos[0]) + abs(cur_right_pos[1] - target_pos[1])  # 왼손과 타겟의 거리

            if left_target_dist < right_target_dist:
                cur_left_pos = target_pos
                result.append('L')
            elif right_target_dist < left_target_dist:
                cur_right_pos = target_pos
                result.append('R')
            elif left_target_dist == right_target_dist:
                if hand == 'left':
                    cur_left_pos = target_pos
                    result.append('L')
                elif hand == 'right':
                    cur_right_pos = target_pos
                    result.append('R')

    return result

result = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
answer = ''.join(result)
result = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
answer = ''.join(result)
result = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
answer = ''.join(result)
print(answer)