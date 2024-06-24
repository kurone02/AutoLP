from pulp import *

# Define the decision variables
# number of large cruise ship trips
num_large_trips = LpVariable("NumLargeTrips", lowBound=0, cat='Integer')
# number of small cruise ship trips
num_small_trips = LpVariable("NumSmallTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CruiseCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total pollution produced
objective = 20 * num_large_trips + 15 * num_small_trips
problem += objective

# Define the constraints
# total customers
problem += 2000 * num_large_trips + 800 * num_small_trips >= 20000
# maximum number of large cruise ship trips
problem += num_large_trips <= 7
# minimum number of small cruise ship trips
problem += num_small_trips >= 0.4 * (num_large_trips + num_small_trips)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of large cruise ship trips:", num_large_trips.value())
print("The number of small cruise ship trips:", num_small_trips.value())
print("Total amount of pollution produced:", objective.value())
print("## end solving")