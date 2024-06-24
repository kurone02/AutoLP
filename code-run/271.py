from pulp import *

# Define the decision variables
# number of regular handbags
num_regular = LpVariable("NumRegular", lowBound=0, cat='Integer')
# number of premium handbags
num_premium = LpVariable("NumPremium", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FashionProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 30 * num_regular + 180 * num_premium
problem += objective

# Define the constraints
# total cost
problem += 200 * num_regular + 447 * num_premium <= 250000
# total number of handbags
problem += num_regular + num_premium <= 475

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular handbags:", num_regular.value())
print("The number of premium handbags:", num_premium.value())
print("The monthly profit:", objective.value())
print("## end solving")