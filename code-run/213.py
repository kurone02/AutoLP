from pulp import *

# Define the decision variables
# number of otters
num_otters = LpVariable("NumOtters", lowBound=0, cat='Integer')
# number of dolphins
num_dolphins = LpVariable("NumDolphins", lowBound=10, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("AquariumProblem", LpMaximize)

# Define the objective function
# maximize the total number of tricks performed
objective = 3 * num_otters + 1 * num_dolphins
problem += objective

# Define the constraints
# total treats available
problem += 3 * num_otters + 5 * num_dolphins <= 200
# at most 30% of the performers can be otters
problem += num_otters <= 0.3 * (num_otters + num_dolphins)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of otters:", num_otters.value())
print("The number of dolphins:", num_dolphins.value())
print("The number of tricks performed:", objective.value())
print("## end solving")