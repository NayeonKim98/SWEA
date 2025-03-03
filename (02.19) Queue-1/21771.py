def solution(bridge_length, weight, truck_weights):
    time = 0  # 경과 시간
    top = 0  # 현재 다리에 올라갈 트럭의 인덱스
    total_weight = 0  # 현재 다리 위 트럭들의 총 무게
    bridge = [0] * bridge_length  # 다리 위 상태(트럭이 있으면 무게, 없으면 0)

    while top < len(truck_weights) or total_weight > 0:
        time += 1  # 1초 증가

        # 다리를 빠져나가는 트럭 무게 제거
        total_weight -= bridge.pop(0)

        # 새 트럭이 다리에 올라갈 수 있는지 확인
        if top < len(truck_weights) and total_weight + truck_weights[top] <= weight:
            bridge.append(truck_weights[top])  # 새로운 트럭 추가
            total_weight += truck_weights[top]  # 다리 무게 업데이트
            top += 1  # 다음 트럭 준비
        else:
            bridge.append(0)  # 빈 자리 유지

    return time

# 테스트 실행
test_cases = [
    (2, 10, [7, 4, 5, 6]),
    (100, 100, [10]),
    (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
]

for i, (bridge_length, weight, truck_weights) in enumerate(test_cases, 1):
    result = solution(bridge_length, weight, truck_weights)
    print(f"Test Case #{i}: {result}")
