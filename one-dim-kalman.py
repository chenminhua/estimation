from collections import namedtuple
gaussian = namedtuple('Gaussian', ['mean', 'var'])

gaussian.__repr__ = lambda s : '𝒩(μ={:.3f}, 𝜎²={:.3f})'.format(s[0], s[1])

def predict(pos, movement):
  return gaussian(pos.mean + movement.mean, pos.var + movement.var)

def gaussian_multiply(g1, g2):
  mean = (g1.var * g2.mean + g2.var * g1.mean) / (g1.var + g2.var)
  varience = (g1.var * g2.var) / (g1.var + g2.var)
  return gaussian(mean, varience)

def update(prior, likelihood):
  return gaussian_multiply(likelihood, prior)

# pos = gaussian(10., .2**2)
# move = gaussian(15., .7**2)
# measure = gaussian(26., .2**2)
# pred = predict(pos, move)
# print(pred)
# posterior = update(pred, measure)
# print(posterior)

# 预测增加了不确定性，加入测量后又降低了不确定性

class Robot:
  def __init__(self, speed_mu = 0.0):
    self.motor_sensor_var = 1     # 运动传感器的误差
    self.distence_sensor_var = 1  # 距离传感器的误差
    self.belief = gaussian(0, 1)   # 初始位置为0，var = 1

  def run(self, move, measure):
    pred = predict(self.state, gaussian(move, self.motor_sensor_var))
    self.belief = update(pred, gaussian(measure, distence_sensor_var))



  