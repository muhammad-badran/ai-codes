#Code by: Dorsa (Lecture 5)

Class TransportationProblem(object):
  def __init__(self, N):
    # N = Number of blocks
    self.N = N
  def startState(self):
    return 1
  def isEnd(self, state):
    return state == self.N
  def succAndCost(self, state):
    # return list of (action, newState, cost) triples
    result = []
    if state + 1 <= self.N:
      result.append(('walk', state + 1, 1))
    if state * 2 < self.N:
      result.append(('tram', state * 2, 2))
    return result
  
problem = TransportationProblem(N=10)
print(problem.succAndCost(3))
print(problem.succAndCost(9))
