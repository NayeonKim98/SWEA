# 사각형 찾기(11039, sw)
def snail_array(N):
    # 1. N x N 크기의 0으로 채워진 2D 리스트 만들기
    arr = [[0] * N for _ in range(N)]

    # 2. 델타 탐색을 위한 방향 배열 설정 (오른쪽 -> 아래 -> 왼쪽 -> 위)
    dx = [0, 1, 0, -1]  # 행 이동
    dy = [1, 0, -1, 0]  # 열 이동

    x, y, direction = 0, 0, 0  # 시작 위치 (0,0) / 처음 방향: 오른쪽

    # 3. 1부터 N*N까지 숫자 채우기
    for num in range(1, N * N + 1):
        arr[x][y] = num  # 현재 위치에 숫자 넣기

        # 4. 다음 위치 계산
        nx, ny = x + dx[direction], y + dy[direction]

        # 5. 범위를 벗어나거나 이미 숫자가 들어있다면 방향 변경
        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
            direction = (direction + 1) % 4  # 방향 변경 (0→1→2→3 순환)
            nx, ny = x + dx[direction], y + dy[direction]

        # 6. 위치 갱신
        x, y = nx, ny

    return arr  # 달팽이 배열 반환


# 7. 달팽이 배열 출력 함수
def print_array(arr):
    for row in arr:
        print("\t".join(map(str, row)))  # 가독성을 위해 탭("\t")으로 구분


# 실행 예제
N = int(input("달팽이 크기 입력: "))  # 사용자 입력
result = snail_array(N)  # 달팽이 배열 생성
print_array(result)  # 결과 출력