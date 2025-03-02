def solution(priorities, location):
    order = []  # 실행된 프로세스 저장
    visited = [0] * len(priorities)  # 실행된 프로세스를 체크
    top = 0  # 현재 가리키는 프로세스 위치

    while len(order) < len(priorities):  # 모든 프로세스가 실행될 때까지
        max_num = max([priorities[i] for i in range(len(priorities)) if not visited[i]])  # 실행되지 않은 프로세스 중 최댓값

        # 실행되지 않은 프로세스만 확인
        if not visited[top]:  
            if priorities[top] < max_num:  # 더 높은 우선순위가 있다면 다음으로 이동
                top = (top + 1) % len(priorities)
            else:  # 현재 프로세스 실행
                order.append(top)  # 실행된 프로세스의 위치를 저장
                visited[top] = 1  # 실행 완료 표시
                if top == location:  # 원하는 프로세스가 실행되었으면 종료
                    return len(order)
                top = (top + 1) % len(priorities)  # 다음 프로세스로 이동
        else:  # 이미 실행된 프로세스라면 넘어가기
            top = (top + 1) % len(priorities)

    return -1  # 예외 처리 (실제로 발생하지 않음)

# 입력 처리
priorities = list(map(int, input().split()))
location = int(input())

result = solution(priorities, location)
print(result)