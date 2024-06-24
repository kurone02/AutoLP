from pulp import *

# Define the decision variables
# number of acres of winter wheat to plant
acres_wheat = LpVariable("AcresWheat", lowBound=0, cat='Integer')
# number of acres of rye to plant
acres_rye = LpVariable("AcresRye", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 42 * acres_wheat + 35 * acres_rye
problem += objective

# Define the constraints
# total input cost
problem += 90 * acres_wheat + 120 * acres_rye <= 90000
# total labor and machinery cost
problem += 50 * acres_wheat + 40 * acres_rye <= 36000
# total acres planted
problem += acres_wheat + acres_rye <= 800

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of acres of winter wheat to plant:", acres_wheat.value())
print("The number of acres of rye to plant:", acres_rye.value())
print("The maximum profit:", objective.value())

# New objective
objective_new = 40 * acres_wheat + 45 * acres_rye
problem.setObjective(objective_new)

# Solve the new problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the new answer
print("New optimal number of acres of winter wheat to plant:", acres_wheat.value())
print("New optimal number of acres of rye to plant:", acres_rye.value())
print("New maximum profit:", objective_new.value())
print("## end solving")