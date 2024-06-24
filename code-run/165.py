from pulp import *

# Define the decision variables
AmountA = LpVariable("AmountA", lowBound=0, cat='Continuous')
AmountB = LpVariable("AmountB", lowBound=0, cat='Continuous')
AmountC = LpVariable("AmountC", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("SheepFeedingProblem", LpMinimize)

# Define the objective function
problem += 41 * AmountA + 36 * AmountB + 96 * AmountC

# Define the constraints
problem += 20 * AmountA + 30 * AmountB + 70 * AmountC >= 110
problem += 10 * AmountA + 10 * AmountB + 30 * AmountC >= 18
problem += 70 * AmountA >= 90
problem += 6 * AmountA + 2.5 * AmountB + 10 * AmountC >= 14

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of grain A to feed the sheep:", value(AmountA))
print("The amount of grain B to feed the sheep:", value(AmountB))
print("The amount of grain C to feed the sheep:", value(AmountC))
print("The minimum cost:", value(problem.objective))
print("## end solving")