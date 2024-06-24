from pulp import *

# Define the decision variables
# number of units of chemical A
units_A = LpVariable("UnitsA", lowBound=0, cat='Integer')
# number of units of chemical B
units_B = LpVariable("UnitsB", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BreadMixerProblem", LpMinimize)

# Define the objective function
# minimize the total time it takes for the mixed bread to be ready
objective = 30 * units_A + 45 * units_B
problem += objective

# Define the constraints
# at most a third as much chemical A as chemical B in the mixer
problem  += 3*units_A >= units_B # problem += units_A >= units_B / 3
# there has to be at least 300 units of chemical A in the mixer
problem += units_A >= 300
# there has to be at least 1500 units of total chemicals in the mixer
problem += units_A + units_B >= 1500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The units of chemical A:", units_A.value())
print("The units of chemical B:", units_B.value())
print("The total time it takes for the mixed bread to be ready:", objective.value())
print("## end solving")