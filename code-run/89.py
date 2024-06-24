from pulp import *

# Define the decision variables
# number of regular sandwiches
num_regular = LpVariable("NumRegular", lowBound=0, cat='Integer')
# number of special sandwiches
num_special = LpVariable("NumSpecial", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SandwichProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 3 * num_regular + 4 * num_special
problem += objective

# Define the constraints
# total eggs required
problem += 2 * num_regular + 3 * num_special <= 40
# total bacon required
problem += 3 * num_regular + 5 * num_special <= 70

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular sandwiches:", num_regular.value())
print("The number of special sandwiches:", num_special.value())
print("Total profit:", objective.value())
print("## end solving")