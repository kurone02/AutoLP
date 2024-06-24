from pulp import *

# Define the decision variables
# number of Model A pizza ovens to purchase
num_model_A = LpVariable("NumModelA", lowBound=0, cat='Integer')
# number of Model B pizza ovens to purchase
num_model_B = LpVariable("NumModelB", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PizzaPalaceOvensProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 10000 * num_model_A + 8000 * num_model_B
problem += objective

# Define the constraints
# total pizzas produced
problem += 10 * num_model_A + 8 * num_model_B >= 100
# total fuel used
problem += 80 * num_model_A + 70 * num_model_B <= 1000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Model A ovens to purchase:", num_model_A.value())
print("The number of Model B ovens to purchase:", num_model_B.value())
print("Total cost:", objective.value())
print("## end solving")