import math

class BilliardGame:
    def __init__(self, table_width, table_height, myball_pos, target_pos, pockets, ball_radius=0.5):
        self.table_width = table_width
        self.table_height = table_height
        self.myball_pos = myball_pos
        self.target_pos = target_pos
        self.pockets = pockets
        self.ball_radius = ball_radius  

    def calculate_distance(self, point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    def find_best_pocket(self):
        best_pocket = None
        min_distance = float('inf')

        for pocket in self.pockets:
            dist = self.calculate_distance(self.target_pos, pocket) - self.ball_radius
            if dist < min_distance:
                min_distance = dist
                best_pocket = pocket

        return best_pocket
    
    def calculate_shot(self):
        best_pocket = self.find_best_pocket()

        dx_target = self.target_pos[0] - self.myball_pos[0]
        dy_target = self.target_pos[1] - self.myball_pos[1]
        distance_to_target = self.calculate_distance(self.myball_pos, self.target_pos)

        impact_x = self.target_pos[0] - (dx_target/distance_to_target) * self.ball_radius
        impact_y = self.target_pos[1] - (dy_target/distance_to_target) * self.ball_radius

        angle_to_target = math.degrees(math.atan2(impact_y - self.myball_pos[1], impact_x - self.myball_pos[0]))

        dx_pocket = best_pocket[0] - self.target_pos[0]
        dy_pocket = best_pocket[1] - self.target_pos[1]
        angle_to_pocket = math.degrees(math.atan2(dy_pocket, dx_pocket))

        shot_angle = 2 * angle_to_pocket - angle_to_target

        total_distance = self.calculate_distance(self.myball_pos, (impact_x, impact_y)) + \
                         self.calculate_distance(self.target_pos, best_pocket) - self.ball_radius
        
        power = min(max(total_distance,* 5, 10), 100)

        return shot_angle % 360, power
    
    def play(self):
        shot_angle, power = self.calculate_shot()
        
        if shot_angle is not None:
            print(f"\n🚀 공을 {power:.2f}의 힘으로 {shot_angle:.2f}° 방향으로 칩니다!")
        else:
            print("❌ 적절한 샷을 찾을 수 없습니다.")