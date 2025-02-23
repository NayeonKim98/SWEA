import math

class Billiard:
    """🎱 당구 게임 시뮬레이션 클래스"""
    
    def __init__(self, table_width, table_height, cue_ball_pos, target_ball_pos):
        """
        📌 당구대 초기화
        :param table_width: 당구대 가로 길이
        :param table_height: 당구대 세로 길이
        :param cue_ball_pos: 큐볼(치는 공)의 좌표 (x, y)
        :param target_ball_pos: 목표 공의 좌표 (x, y)
        """
        self.table_width = table_width
        self.table_height = table_height
        self.cue_ball_pos = cue_ball_pos
        self.target_ball_pos = target_ball_pos

    def calculate_angle_and_power(self):
        """
        🎯 두 공 사이의 거리 및 각도를 계산하여 샷의 방향과 힘을 결정
        :return: (angle, power) → 각도(라디안), 파워(거리 기반)
        """
        # 목표 공과 큐볼 사이의 x, y 차이 계산
        dx = self.target_ball_pos[0] - self.cue_ball_pos[0]
        dy = self.target_ball_pos[1] - self.cue_ball_pos[1]

        # 유클리드 거리 공식 사용
        distance = math.sqrt(dx**2 + dy**2)

        # atan2()를 이용해 각도(라디안) 계산 후 0~360도로 변환
        angle = math.degrees(math.atan2(dy, dx)) % 360  

        # 거리에 비례한 파워 설정 (최소 10, 최대 100)
        power = min(max(distance * 10, 10), 100)

        return angle, power

    def simulate_shot(self, angle, power):
        """
        🚀 공을 주어진 각도와 파워로 굴려보는 시뮬레이션
        - 간단한 물리 구현 (직선 이동 + 벽 반사)
        :param angle: 공을 치는 각도 (도 단위)
        :param power: 공을 치는 힘
        :return: (최종 공 위치 x, y)
        """
        # 라디안으로 변환 (cos, sin 사용을 위해)
        angle_rad = math.radians(angle)

        # 공의 초기 위치 설정
        x, y = self.cue_ball_pos

        # 공이 이동하는 방향 벡터 계산
        vx = power * math.cos(angle_rad) * 0.1  # 속도 (0.1은 시간 단위)
        vy = power * math.sin(angle_rad) * 0.1

        # 공이 벽에 부딪힐 경우 반사 처리
        while True:
            x += vx
            y += vy

            # 왼쪽 벽(0) 또는 오른쪽 벽(table_width)에 부딪힌 경우 x 반전
            if x <= 0 or x >= self.table_width:
                vx *= -1  # x축 방향 반전
                x = max(0, min(x, self.table_width))  # 범위 제한

            # 위쪽 벽(0) 또는 아래쪽 벽(table_height)에 부딪힌 경우 y 반전
            if y <= 0 or y >= self.table_height:
                vy *= -1  # y축 방향 반전
                y = max(0, min(y, self.table_height))  # 범위 제한

            # 목표 공 근처에 도달하면 종료
            if math.sqrt((x - self.target_ball_pos[0])**2 + (y - self.target_ball_pos[1])**2) < 0.5:
                break

        # 최종 공 위치 반환
        return x, y

# 🏆 당구대 크기, 공 위치 설정 (예제)
table_width = 10      # 당구대 가로 길이
table_height = 5      # 당구대 세로 길이
cue_ball_pos = (1, 1)  # 큐볼 위치
target_ball_pos = (8, 3)  # 목표 공 위치

# 🎱 당구 게임 객체 생성
billiard = Billiard(table_width, table_height, cue_ball_pos, target_ball_pos)

# 🏹 각도 및 파워 계산
angle, power = billiard.calculate_angle_and_power()

# 🚀 샷 시뮬레이션 실행
final_x, final_y = billiard.simulate_shot(angle, power)

# 📌 결과 출력
print("\n🎯 당구 시뮬레이션 결과 🎯")
print(f"🔹 샷 각도: {angle:.2f}°")
print(f"🔸 샷 파워: {power:.2f}")
print(f"🎱 공의 최종 위치: ({final_x:.2f}, {final_y:.2f})")
