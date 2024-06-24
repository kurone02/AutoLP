from pulp import *

# Define the decision variables
# number of hectares of tomatoes
num_hectares_tomatoes = LpVariable("HectaresTomatoes", lowBound=20, cat='Continuous')
# number of hectares of potatoes
num_hectares_potatoes = LpVariable("HectaresPotatoes", lowBound=30, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FarmerProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 350 * num_hectares_tomatoes + 600 * num_hectares_potatoes
problem += objective

# Define the constraints
# total acres planted
problem += num_hectares_tomatoes + num_hectares_potatoes <= 140
# soil and weather conditions
problem += num_hectares_tomatoes <= 2 * num_hectares_potatoes

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of hectares for tomatoes:", num_hectares_tomatoes.value())
print("The number of hectares for potatoes:", num_hectares_potatoes.value())
print("The maximum profit is:", objective.value())
print("## end solving")