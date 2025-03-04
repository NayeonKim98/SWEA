import math

class BilliardSimulation:
    """ 🎱 당구 게임 공 이동 및 충돌 계산 클래스 """
    
    def __init__(self, table_width, table_height, myball_pos, target_pos):
        """
        📌 당구대 초기화
        :param table_width: 당구대 가로 길이
        :param table_height: 당구대 세로 길이
        :param myball_pos: 내 공(큐볼)의 좌표 (x, y)
        :param target_pos: 목표 공(타겟)의 좌표 (x, y)
        """
        self.table_width = table_width
        self.table_height = table_height
        self.myball_pos = myball_pos
        self.target_pos = target_pos

    def calculate_distance(self):
        """
        📏 피타고라스 정리를 이용하여 두 공 사이 거리 계산
        :return: 두 공 사이의 거리
        """
        dx = self.target_pos[0] - self.myball_pos[0]
        dy = self.target_pos[1] - self.myball_pos[1]
        return math.sqrt(dx**2 + dy**2)

    def move_ball(self, power, angle):
        """
        🚀 공을 주어진 세기와 각도로 이동시키는 시뮬레이션
        :param power: 공을 치는 힘 (거리에 영향을 줌)
        :param angle: 공을 치는 방향 (도 단위)
        :return: (최종 x, 최종 y) - 내 공의 새로운 위치
        """
        # 🎯 각도를 라디안 값으로 변환 (삼각함수 사용을 위해)
        angle_rad = math.radians(angle)

        # 💨 공이 이동할 거리 = 세기(Power)에 비례
        move_distance = power * 0.1  # 0.1은 거리 조정 계수

        # 📌 삼각함수를 이용하여 이동 후 x, y 좌표 계산
        new_x = self.myball_pos[0] + move_distance * math.cos(angle_rad)
        new_y = self.myball_pos[1] + move_distance * math.sin(angle_rad)

        # 🚧 테이블 경계 체크 (벽에 부딪히면 반사)
        if new_x <= 0 or new_x >= self.table_width:
            new_x = max(0, min(new_x, self.table_width))  # 경계 유지

        if new_y <= 0 or new_y >= self.table_height:
            new_y = max(0, min(new_y, self.table_height))  # 경계 유지

        return new_x, new_y

    def check_hit(self, new_x, new_y):
        """
        🎯 목표 공에 맞았는지 체크
        :param new_x: 이동 후 내 공의 x 좌표
        :param new_y: 이동 후 내 공의 y 좌표
        :return: 목표 공에 맞으면 True, 아니면 False
        """
        # 두 공 사이 거리 재계산
        distance = math.sqrt((new_x - self.target_pos[0])**2 + (new_y - self.target_pos[1])**2)
        
        # 🎯 공이 부딪혔다고 판단할 거리 기준 (예: 0.5 이하)
        return distance <= 0.5

    def play(self, power, angle):
        """
        🏆 주어진 세기와 각도로 공을 치고 결과를 확인하는 함수
        :param power: 공을 치는 힘
        :param angle: 공을 치는 방향 (도 단위)
        """
        print(f"\n🚀 공을 {power}의 힘으로 {angle}° 방향으로 칩니다!")

        # 공 이동 시뮬레이션
        new_x, new_y = self.move_ball(power, angle)

        # 목표 공 맞았는지 확인
        if self.check_hit(new_x, new_y):
            print(f"🎯 목표 공을 맞혔습니다! (최종 위치: {new_x:.2f}, {new_y:.2f})")
        else:
            print(f"❌ 목표 공을 맞히지 못했습니다. (최종 위치: {new_x:.2f}, {new_y:.2f})")

# 🏆 당구대 크기 및 공 위치 설정
table_width = 10  # 가로 길이
table_height = 5  # 세로 길이
myball_pos = (1, 1)  # 내 공 위치
target_pos = (8, 3)  # 목표 공 위치

# 🎱 당구 시뮬레이션 객체 생성
billiard_game = BilliardSimulation(table_width, table_height, myball_pos, target_pos)

# 🔥 공을 치는 세기와 각도 입력
power = 80  # 세기
angle = 20  # 각도 (0° = 오른쪽 방향)

# 🎯 게임 실행
billiard_game.play(power, angle)
