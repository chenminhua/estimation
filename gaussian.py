import numpy as np
import matplotlib.pyplot as plt

class GaussianDist:
  
  def __init__(self, mu, var):
    self.mu = mu
    self.var = var

  def at(self, x):
    
    exp_term = np.exp(-((x - self.mu) * (x - self.mu)) / (2. * self.var))
    return (1. / np.sqrt(2 * 3.1416 * self.var)) * exp_term
  
  def multiply(self, g):
    # g为另一个高斯分布
    mu = (self.var * g.mu + g.var * self.mu) / (self.var + g.var)
    var = (self.var * g.var) / (self.var + g.var)
    return GaussianDist(mu, var)

  def __repr__(self):
    return "N({}, {})".format(self.mu, self.var)

xlist = np.linspace(-4,4,200)

g1 = GaussianDist(-1,4)
g2 = GaussianDist(1,1)
g3 = g1.multiply(g2)
print("N(0, 1) * N(0, 1): ", g3)

plt.plot(xlist, [g1.at(x) for x in xlist], label = "N(-1,4)")
plt.plot(xlist, [g2.at(x) for x in xlist], label = "N(1,1)")
plt.plot(xlist, [g3.at(x) for x in xlist], label = "N(-1,4) * N(1,1) = {}".format(g3))
plt.legend()
plt.show()