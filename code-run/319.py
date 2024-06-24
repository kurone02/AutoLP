from pulp import *

# Define the decision variables
# number of motorcycles
num_motorcycles = LpVariable("NumMotorcycles", lowBound=0, cat='Integer')
# number of sedans
num_sedans = LpVariable("NumSedans", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("TaxiCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total earnings
objective = 100 * num_motorcycles + 225 * num_sedans
problem += objective

# Define the constraints
# total number of people
problem += 30 * num_motorcycles + 70 * num_sedans >= 1200
# total units of pollution
problem += 4 * num_motorcycles + 15 * num_sedans <= 200
# at most 25% of vehicles can be motorcycles
problem += num_motorcycles <= 0.25 * (num_motorcycles + num_sedans)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of motorcycles:", num_motorcycles.value())
print("The number of sedans:", num_sedans.value())
print("Total earnings per shift:", objective.value())
print("## end solving")