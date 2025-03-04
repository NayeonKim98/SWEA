def dfs(row, total):
    global min_sum  # 최소 합을 저장하는 전역 변수

    # ✅ 가지치기 (현재 합이 기존 최소값보다 크면 더 이상 탐색할 필요 없음)
    if total >= min_sum:
        return

    # ✅ 모든 행을 탐색 완료한 경우 최소값 갱신
    if row == N:
        min_sum = min(min_sum, total)
        return

    # ✅ 현재 행(row)에서 가능한 숫자를 선택하여 다음 행으로 이동
    for col in range(N):  # 모든 열을 탐색
        if visited[col] == 0:  # 같은 열에서 선택되지 않은 숫자만 선택
            visited[col] = 1  # 방문 체크 (열 선택)
            dfs(row + 1, total + board[row][col])  # 다음 행 탐색 (재귀 호출)
            visited[col] = 0  # 🔥 백트래킹 (이전 상태로 복구)

# ✅ 입력 처리 및 실행
T = 1  # 테스트 케이스 개수
N = 3  # 배열 크기 (3x3)
board = [
    [1, 2, 3],  # 0번 행
    [4, 5, 6],  # 1번 행
    [7, 8, 9]   # 2번 행
]

visited = [0] * N  # 세로줄 방문 체크 (처음엔 모두 0)
min_sum = float('inf')  # 최소 합 초기화 (최대값으로 설정)

dfs(0, 0)  # 🔥 백트래킹 탐색 시작 (첫 번째 행, 합 = 0부터 시작)

print(f"최소 합: {min_sum}")  # ✅ 결과 출력