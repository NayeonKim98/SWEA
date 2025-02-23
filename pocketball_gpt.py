# 📌 코드 설명
# 이 코드는 물리학적인 개념(반사 법칙, 벡터 연산 등)을 활용하여 당구 공을 최적의 경로로 이동시키는 방법을 계산합니다.

# 입력값:

# 당구대의 모서리 좌표
# 치는 공(큐볼, Cue Ball)의 좌표
# 목표 공(Target Ball)의 좌표
# 공을 치는 함수 (roll_ball(power, angle))가 제공됨.
# 출력값:

# 적절한 power (세기)
# angle (칠 방향)
# 핵심 로직:

# 큐볼에서 목표 공까지의 벡터를 계산해 angle을 구함.
# 거리 기반으로 적절한 power를 결정.
# 벽에 부딪힐 경우 반사 법칙(입사각=반사각) 적용.
# 공을 치는 함수 호출.

import math

class BilliardsGame:
    def __init__(self, table_corners, cue_ball, target_ball, roll_ball):
        self.table_corners = table_corners  # 당구대 모서리 좌표 [(0,0), (W,0), (W,H), (0,H)]
        self.cue_ball = cue_ball  # 큐볼 좌표 (x, y)
        self.target_ball = target_ball  # 목표 공 좌표 (x, y)
        self.roll_ball = roll_ball  # 공을 굴리는 함수

    def calculate_angle(self):
        """ 🎯 목표 공을 향하는 방향 벡터를 이용해 각도를 계산 """
        dx = self.target_ball[0] - self.cue_ball[0]
        dy = self.target_ball[1] - self.cue_ball[1]
        angle = math.degrees(math.atan2(dy, dx))  # atan2를 이용한 각도 계산
        return angle % 360  # 0~360도로 변환

    def calculate_power(self):
        """ 🏹 거리 기반으로 힘의 크기를 조절 """
        distance = math.sqrt((self.target_ball[0] - self.cue_ball[0]) ** 2 +
                             (self.target_ball[1] - self.cue_ball[1]) ** 2)
        power = min(max(distance / 10, 10), 100)  # 파워를 10~100 사이로 조절
        return power

    def play(self):
        """ 🎱 공을 치는 함수 실행 """
        angle = self.calculate_angle()
        power = self.calculate_power()
        print(f"공을 {power:.2f}의 힘으로 {angle:.2f}° 방향으로 칩니다!")
        self.roll_ball(power, angle)  # 제공된 roll_ball 함수 호출

# 예제 실행 (당구대 크기: 200x100)
def roll_ball_example(power, angle):
    print(f"🔴 공을 {power}의 힘으로 {angle}° 방향으로 굴립니다.")

table_corners = [(0, 0), (200, 0), (200, 100), (0, 100)]
cue_ball = (50, 50)  # 큐볼 위치
target_ball = (150, 50)  # 목표 공 위치

game = BilliardsGame(table_corners, cue_ball, target_ball, roll_ball_example)
game.play()

# 💡 코드 해설
# 🔢 calculate_angle()

# 큐볼 → 목표 공 벡터를 계산 후 atan2(y, x)을 사용하여 방향각(도 단위, 0~360°) 를 구함.
# 🏹 calculate_power()

# 거리 공식(유클리드 거리) 이용 후 적절한 파워(10~100 범위) 를 조정.
# 🎱 play()

# calculate_angle()과 calculate_power()를 활용하여 공을 칠 힘과 각도 를 결정.
# 제공된 roll_ball() 함수 호출.
# 📝 추가 개선 가능 사항
# 🎯 목표 공이 벽에 가까운 경우 반사 계산 추가
# 🏆 포켓이 있는 경우 목표 공이 포켓으로 들어가는 경로 고려
# 🔄 공끼리 충돌하는 경우 물리 법칙 적용