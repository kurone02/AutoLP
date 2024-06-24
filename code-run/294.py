from pulp import *

# Define the decision variables
# number of burgers
num_burgers = LpVariable("NumBurgers", lowBound=0, cat='Integer')
# number of pizza slices
num_pizza_slices = LpVariable("NumPizzaSlices", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ManWeightLossProblem", LpMinimize)

# Define the objective function
# minimize the total cholesterol intake
objective = 12 * num_burgers + 10 * num_pizza_slices
problem += objective

# Define the constraints
# total fat
problem += 10 * num_burgers + 8 * num_pizza_slices >= 130
# total calories
problem += 300 * num_burgers + 250 * num_pizza_slices >= 3000
# pizza slices constraint
problem += num_pizza_slices >= 2 * num_burgers

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of burgers to eat:", num_burgers.value())
print("The number of slices of pizza to eat:", num_pizza_slices.value())
print("The minimum cholesterol intake:", objective.value())
print("## end solving")