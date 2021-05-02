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
  
# Gradient Descent
def F(w):
  return sum((w.dot(x) - y)**2 for x, y in points) / len(points)

def dF(w):
  return sum(2*(w.dot(x) - y) * x for x, y in points) / len(points)

# Stocastic Gradient Descent
def sF(w, i):
  x , y = points[i]
  return sum((w.dot(x) - y)**2

def sdF(w, i):
  x , y = points[i]
  return 2*(w.dot(x) - y) * x



#####################################

# Algorithms: how we compute it

def gradientDescent(F, dF, d):
  # Gradient descent
  w = np.zeros(d)
  eta = 0.01
  for t in range(1000):
    value = F(w)
    gradient = dF(w)
    w = w - eta * gradient
    print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))

def stocasticGradientDescent(sF, sdF, d, n):
  # Stocastic Gradient descent
  w = np.zeros(d)
  eta = 1
  numUpdates = 0
  for t in range(1000):
    for i in range(n):
      value = sF(w, i)
      gradient = sdF(w, i)   
      numUpdates += 1
      eta = 1.0 / numUpdates
      w = w - eta * gradient
    print('iteration {}: w = {}, F(w) = {}'.format(t, w, value))
             
             
gradientDescent(F, df, d)
