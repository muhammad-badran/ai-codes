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

## Algorithms
def printSolution(solution):
  totalCost, history = solution
  print('total cost: {}'.format(totalCost))
  for item in hisotry:
    print(item)

def backtrackingSearch(problem):
  # Best solution found so far (dictionary because of python scoping technicaility)
  best = {
    'cost': float(+inf),
    'history': None
  }
  def recurse(state, history, totalCost):
    # At state, having undergone history, accumulated total cost.
    # Explore the rest of the subtree under state.
    
    if problem.isEnd(state):
      # Update the best solution so far
      if totalCost < best['cost']:
        best['cost'] = totalCost
        best['history'] = history
     return
  # Recurse of children
  for action, newState, cost in problem.succAndCost(state):
    recurse(newState, history+[(action, newState, cost)], totalCost + cost
            
  recurse(problem.startState(), history[], totalCost = 0)
  return (best['cost'], best['history'])
  
def dynamicProgramming(problem):
  cache = {} # state -> futureCost(state)
            
  def futureCost(state):
     # Base Case
     if problem.isEnd(state):
        return 0
     if state in cache:
        return cache[state]
     result = min (cost+futureCost(newState) \ for action, newState, cost in problem.succAndCost(state))
     cache[state] = result
     return result       
  return (futureCost(problem.statState(), [])
  
  
  
problem = TransportationProblem(N=10)
print(problem.succAndCost(3))
print(problem.succAndCost(9))
