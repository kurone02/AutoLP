from pulp import *

# Define the decision variables
# number of trains
num_trains = LpVariable("NumTrains", lowBound=0, cat='Integer')
# number of trams
num_trams = LpVariable("NumTrams", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("RailwayInfrastructureProblem", LpMinimize)

# Define the objective function
# minimize the total number of transportation units
objective = num_trains + num_trams
problem += objective

# Define the constraints
# number of people that can be transported per hour
problem += 120 * num_trains + 30 * num_trams >= 600
# the number of trams must be at least twice the number of trains
problem += num_trams >= 2 * num_trains

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of trains:", num_trains.value())
print("The number of trams:", num_trams.value())
print("The total number of transportation units:", objective.value())
print("## end solving")