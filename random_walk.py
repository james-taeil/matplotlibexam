from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:

            # 어느 방향으로 갈지. 얼마만큼 갈지 정한다.
            x_direction = choice([1, -1]) #1  오른쪽 //-1 왼쪽
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance # 거리와 방향을 곱해서 얼만큼 움직일지 계산

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # 모두  0이면 움직임이 없는 단계로 버린다.
            # x_step이 양수:오른쪽 음수:왼쪽
            # y_step이 양수:위로 음수:아래로

            if x_step == 0 and y_step == 0 :
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)