import math

class Billiard:
    def __init__(self, table_width, table_height, cue_ball_pos, target_ball_pos):
        self.table_width = table_width
        self.table_height = table_height
        self.cue_ball_pos = cue_ball_pos
        self.target_ball_pos = target_ball_pos

    def calculate_angle_and_power(self):
        # 두 공 사이의 거리 및 각도 계산
        dx = self.target_ball_pos[0] - self.cue_ball_pos[0]
        dy = self.target_ball_pos[1] - self.cue_ball_pos[1]
        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)

        # 파워는 거리에 비례하도록 설정 (조절 가능)
        power = distance * 10 

        return angle, power

    def simulate_shot(self, angle, power):
        # 간단한 시뮬레이션: 직선으로 공이 움직인다고 가정
        # 실제 당구는 마찰, 회전 등 복잡한 요소가 작용하므로 정확한 시뮬레이션에는 한계가 있음
        
        x = self.cue_ball_pos[0]
        y = self.cue_ball_pos[1]
        
        # 공이 테이블 밖으로 나가지 않도록 처리
        while 0 <= x <= self.table_width and 0 <= y <= self.table_height:
            x += power * math.cos(angle) * 0.1 # 0.1은 임의의 시간 간격
            y += power * math.sin(angle) * 0.1

        # 시뮬레이션 결과 반환 (테이블 밖으로 나갔는지 여부, 최종 위치 등)
        return not (0 <= x <= self.table_width and 0 <= y <= self.table_height), x, y

# 당구대 크기, 공 위치 설정 (예시)
table_width = 10
table_height = 5
cue_ball_pos = (1, 1)
target_ball_pos = (8, 3)

# 당구 게임 객체 생성
billiard = Billiard(table_width, table_height, cue_ball_pos, target_ball_pos)

# 각도 및 파워 계산
angle, power = billiard.calculate_angle_and_power()

# 샷 시뮬레이션
is_out, final_x, final_y = billiard.simulate_shot(angle, power)

# 결과 출력
print(f"각도: {math.degrees(angle)}도")
print(f"파워: {power}")
if is_out:
    print("공이 테이블 밖으로 나갔습니다.")
else:
    print(f"공의 최종 위치: ({final_x:.2f}, {final_y:.2f})")

# Billiard 클래스:

# 당구대 크기, 공 위치 정보를 저장합니다.
# calculate_angle_and_power(): 두 공 사이의 각도와 거리를 계산하여 샷의 각도와 파워를 결정합니다.
# simulate_shot(): 계산된 각도와 파워로 공을 굴리는 시뮬레이션을 수행합니다. (단순한 직선 운동 모델)
# 게임 설정:

# 당구대 크기, 큐 공 위치, 목표 공 위치를 설정합니다.
# 당구 게임 객체 생성:

# Billiard 클래스의 인스턴스를 생성하여 당구 게임을 초기화합니다.
# 각도 및 파워 계산:

# calculate_angle_and_power() 메서드를 호출하여 샷의 각도와 파워를 계산합니다.
# 샷 시뮬레이션:

# simulate_shot() 메서드를 호출하여 공을 굴리는 시뮬레이션을 수행합니다.
# 결과 출력:

# 계산된 각도, 파워, 시뮬레이션 결과를 출력합니다.
# 추가 설명
# 시뮬레이션의 한계: 위 코드는 매우 단순한 시뮬레이션으로, 실제 당구의 물리적 특성 (마찰, 회전 등)을 고려하지 않았습니다. 더 정확한 시뮬레이션을 위해서는 복잡한 물리 엔진을 사용해야 합니다.
# 파워 조절: 파워는 거리에 비례하도록 설정되었지만, 실제 게임에서는 다양한 요소 (공의 무게, 마찰 등)를 고려하여 파워를 조절해야 합니다.
# 인터페이스: 위 코드는 텍스트 기반으로 결과를 출력하지만, Pygame과 같은 라이브러리를 사용하면 당구 게임을 시각적으로 구현할 수 있습니다.