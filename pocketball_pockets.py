import math

class BilliardGame:
    """ 🎱 당구 게임 시뮬레이션: 목적구를 포켓으로 넣는 로직 포함 """

    def __init__(self, table_width, table_height, myball_pos, target_pos, pockets):
        """
        📌 당구대 초기화
        :param table_width: 당구대 가로 길이
        :param table_height: 당구대 세로 길이
        :param myball_pos: 내 공(큐볼)의 좌표 (x, y)
        :param target_pos: 목표 공(타겟)의 좌표 (x, y)
        :param pockets: 포켓들의 좌표 리스트 [(x1, y1), (x2, y2), ...]
        """
        self.table_width = table_width
        self.table_height = table_height
        self.myball_pos = myball_pos
        self.target_pos = target_pos
        self.pockets = pockets  # 포켓 위치 리스트

    def calculate_distance(self, point1, point2):
        """
        📏 두 점(point1, point2) 사이 거리 계산 (피타고라스 정리 활용)
        :return: 유클리드 거리
        """
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    def find_best_pocket(self):
        """
        🎯 목적구를 가장 쉽게 넣을 수 있는 포켓 선택
        :return: 가장 가까운 포켓 좌표
        """
        best_pocket = None
        min_distance = float('inf')

        for pocket in self.pockets:
            dist = self.calculate_distance(self.target_pos, pocket)
            if dist < min_distance:
                min_distance = dist
                best_pocket = pocket

        return best_pocket

    def calculate_shot(self):
        """
        🚀 내 공이 목표 공을 맞히고, 목표 공이 포켓으로 들어갈 경로 계산
        :return: (샷 각도, 파워)
        """
        best_pocket = self.find_best_pocket()  # 가장 가까운 포켓 찾기
        
        if not best_pocket:
            print("❌ 적절한 포켓을 찾을 수 없습니다.")
            return None, None

        # 1️⃣ 내 공 → 목표 공 방향 계산
        dx_target = self.target_pos[0] - self.myball_pos[0]
        dy_target = self.target_pos[1] - self.myball_pos[1]
        angle_to_target = math.degrees(math.atan2(dy_target, dx_target))

        # 2️⃣ 목표 공 → 포켓 방향 계산
        dx_pocket = best_pocket[0] - self.target_pos[0]
        dy_pocket = best_pocket[1] - self.target_pos[1]
        angle_to_pocket = math.degrees(math.atan2(dy_pocket, dx_pocket))

        # 🎱 목표 공을 적절한 방향으로 맞추기 위해 내 공이 쳐야 할 각도 계산
        shot_angle = 2 * angle_to_pocket - angle_to_target

        # 🔥 거리 기반 파워 설정 (거리 비례)
        total_distance = self.calculate_distance(self.myball_pos, self.target_pos) + \
                         self.calculate_distance(self.target_pos, best_pocket)
        power = min(max(total_distance * 5, 10), 100)  # 최소 10, 최대 100 조정

        return shot_angle % 360, power

    def play(self):
        """
        🏆 샷 실행 및 결과 출력
        """
        shot_angle, power = self.calculate_shot()
        
        if shot_angle is not None:
            print(f"\n🚀 공을 {power:.2f}의 힘으로 {shot_angle:.2f}° 방향으로 칩니다!")
        else:
            print("❌ 적절한 샷을 찾을 수 없습니다.")


# 🏆 Stage 1~4 설정 (테이블 크기 및 공 배치)
table_width = 10  # 가로 길이
table_height = 5  # 세로 길이
pockets = [(0, 0), (table_width, 0), (table_width, table_height), (0, table_height)]  # 네 모서리에 포켓 존재

# Stage 별 공 배치 (예제)
stages = [
    {"myball": (1, 1), "target": (8, 3)},  # Stage 1
    {"myball": (2, 2), "target": (7, 4)},  # Stage 2
    {"myball": (1, 3), "target": (6, 2)},  # Stage 3
    {"myball": (3, 2), "target": (7, 3)}   # Stage 4 (2개 이상 처리 추가 가능)
]

# 각 스테이지 실행
for i, stage in enumerate(stages, start=1):
    print(f"\n🎯 Stage {i} 시작!")
    billiard_game = BilliardGame(table_width, table_height, stage["myball"], stage["target"], pockets)
    billiard_game.play()
