from pulp import *

# Define the variables
num_cream_lipsticks = LpVariable("NumCreamLipsticks", lowBound=0, cat='Integer')
num_matte_lipsticks = LpVariable("NumMatteLipsticks", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("BobFashionProblem", LpMaximize)
objective = 70 * num_cream_lipsticks + 100 * num_matte_lipsticks
problem += objective

# Define the constraints
problem += 3.5 * num_cream_lipsticks + 5 * num_matte_lipsticks <= 300
problem += 5 * num_cream_lipsticks + 3 * num_matte_lipsticks <= 400
problem += 2 * num_cream_lipsticks + 1.5 * num_matte_lipsticks <= 200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of cream lipsticks to be produced:", num_cream_lipsticks.value())
print("The number of matte lipsticks to be produced:", num_matte_lipsticks.value())
print("The total monthly profit:", objective.value())
print("## end solving")