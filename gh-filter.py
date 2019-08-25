import matplotlib.pyplot as plt
import numpy as np
class Robot:
  def __init__(self, state=0, speed=0, g=0.9, h=0.9):
    self.state = state
    self.speed = speed
    # 机器人的实际位置
    self.actual_locations = [state]
    self.measure_locations = []
    self.measure_speed = 0.0
    self.estimate_locations = [0.0]
    self.est_state = 0.0  # 初始位置不知道在哪，就先0吧
    self.g = g
    self.h = g
  
  # 这是一个只会做匀加速运动的机器人（匀速运动也是一种匀加速运动）
  def run(self, acc=0, t=0):
    if t <= 0: return
    for i in range(t):
      s1 = self.speed
      s2 = self.speed + acc
      self.state += (s1 + s2) / 2.0
      self.speed = s2

      # 测量位置等于实际位置加测量噪声
      measure_state = self.state + self.speed * np.random.randn()

      # 预测位置等于上一个时刻的预测位置 + 机器人认为的自己的速度
      pred_state = self.est_state + self.measure_speed * 1.

      # residual 测量与预测的差距
      residual = measure_state - pred_state

      # 根据 residual 和上一个时刻机器人认为的自己的位置计算新的速度
      self.measure_speed = self.measure_speed + self.h * residual / 1.

      # 结合测量与预测估计当前位置
      self.est_state = pred_state + self.g * residual

      self.actual_locations.append(self.state)
      self.measure_locations.append(measure_state)
      self.estimate_locations.append(self.est_state)

  def show_locatons(self):
    plt.plot(range(len(self.actual_locations)), self.actual_locations, 'b', label="actual loc")
    plt.plot(range(1, len(self.measure_locations) + 1), self.measure_locations, 'y', label="measure loc")
    plt.plot(range(len(self.estimate_locations)), self.estimate_locations, 'r', label="estimate loc")
    plt.legend()
    plt.xlabel("time")
    plt.ylabel("distance")
    plt.show()


robot = Robot()
robot.run(1,8)
robot.run(0,3)
robot.run(-1,8)
robot.show_locatons()
