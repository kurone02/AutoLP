from pulp import *

# Define the decision variables
num_trailer = LpVariable("NumTrailer", lowBound=0, cat='Integer')
num_tanker = LpVariable("NumTanker", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HydrogenTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total number of trips
objective = num_trailer + num_tanker
problem += objective

# Define the constraints
# total volume of hydrogen transported
problem += 50 * num_trailer + 30 * num_tanker >= 300
# total cost of transportation
problem += 500 * num_trailer + 200 * num_tanker <= 3750
# number of high-pressure tube trailer transports less than the number of liquefied hydrogen tanker transports
problem += num_trailer <= num_tanker

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of high-pressure tube trailer transports:", num_trailer.value())
print("The number of liquefied hydrogen tanker transports:", num_tanker.value())
print("The total number of trips:", objective.value())
print("## end solving")