from pulp import *

# Define the decision variables
# number of basketballs
num_basketballs = LpVariable("NumBasketballs", lowBound=0, cat='Integer')
# number of footballs
num_footballs = LpVariable("NumFootballs", lowBound=50, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SportsEquipmentProblem", LpMaximize)

# Define the objective function
# maximize the total number of sports equipment produced
objective = num_basketballs + num_footballs
problem += objective

# Define the constraints
# materials constraint
problem += 5 * num_basketballs + 3 * num_footballs <= 1500
# labor constraint
problem += 1 * num_basketballs + 2 * num_footballs <= 750
# at least three times as many basketballs as footballs constraint
problem += num_basketballs >= 3 * num_footballs
# at least 50 footballs constraint
problem += num_footballs >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of basketballs:", num_basketballs.value())
print("The number of footballs:", num_footballs.value())
print("The total number of sports equipment produced:", objective.value())
print("## end solving")