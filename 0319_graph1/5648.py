# 이동 방향 (상:0, 하:1, 좌:2, 우:3)
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def simulate_atomic_collisions(n, atoms):
    pass

T = int(input())
for tc in range(1, T + 1):
    n = int(input())  # 원자 개수
    atoms = [tuple(map(int, input().split())) for _ in range(n)]  # 원자 정보 입력
    result = simulate_atomic_collisions(n, atoms)
    print(f'#{tc} {result}')