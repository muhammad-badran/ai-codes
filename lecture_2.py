# code by: scherzo (lecture 2)

import numpy as np
#########################################
# Modeling: What we want to compute

#Generate artificial data
ture_w = np.array([1, 2, 3, 4, 5])
d = len(true_w)

points = []

for i in range(1000):
  x = np.random.randn(d)
  y = true_w.dot(x) + np.random.randn()
  #print(x,y)
  points.append((x, y))
  
def F(w):
  return sum((w.dot(x) - y)**2 for x, y in points) / len(points)

def dF(w):
  return sum(2*(w.dot(x) - y) * x for x, y in points) / len(points)
  
#####################################

# Algorithms: how we compute it

def gradientDescent(F, dF, d):
  # Gradient descent
  w = np.zeros(d)
  eta = 0.01
  for t in range(100):
    value = F(w)
    gradient = dF(w)
    w = w - eta * gradient
    print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))

gradientDescent(F, df, d)
