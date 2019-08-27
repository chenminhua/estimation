import numpy as np
h = np.array([1,1,0,0,0,0,0,0,1,0])

def normalize(arr):
  return arr / sum(arr)

class Robot:
  def __init__(self, room, firstread):
    self.room = room
    # 初始状态下机器人完全不知道自己在哪儿
    self.belief = np.array([1./len(room)] * len(room))
    self.measure(firstread)
  
  def measure(self, read):
    # 摄像头可能出现误判，假设摄像头正确率为0.75
    measure_create_rate = 0.75
    scale = measure_create_rate / (1- measure_create_rate)
    likelihood = np.ones(len(self.room))
    likelihood[self.room==read] *= scale
    self.belief = normalize(likelihood * self.belief)  
  
  def rotate(self, move, read):
    # 80%的可能是对的，各10%偏一步。
    # 比如机器人说它转了2步，其实可能转了1步，也可能转了3步
    rotate_kernel = (.1, .8, .1)
    # 先来预测一波
    self.predict(move, rotate_kernel)
    # 在加入测量信息
    self.measure(read)

  def predict(self, offset, kernel):
    N = len(self.belief)
    kN = len(kernel)
    width = int((kN - 1) / 2)

    result = np.zeros(N)
    for i in range(N):
        for k in range (kN):
            index = (i + (width-k) - offset) % N
            result[i] += self.belief[index] * kernel[k]
    self.belief[:] = result[:] # update belief


# 机器人第一眼看到的是门
robot = Robot(h, 1)
print(robot.belief)
# 转了1下看见了门
robot.rotate(1, 1)
print(robot.belief)
robot.rotate(1, 0)
print(robot.belief)
robot.rotate(1, 0)
print(robot.belief)
robot.rotate(1, 0)
print(robot.belief)
robot.rotate(1, 0)
print(robot.belief)
robot.rotate(1, 0)
print(robot.belief)
robot.rotate(1, 0)
print(robot.belief)
robot.rotate(1, 1)
print(robot.belief)
robot.rotate(1, 0)
print(robot.belief)


