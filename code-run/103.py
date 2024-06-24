from pulp import *

# Define the decision variables
# number of model trains
num_trains = LpVariable("NumTrains", lowBound=0, cat='Integer')
# number of model planes
num_planes = LpVariable("NumPlanes", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("TrainPlaneProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 8 * num_trains + 10 * num_planes
problem += objective

# Define the constraints
# total wood available
problem += 3 * num_trains + 4 * num_planes <= 120
# total paint available
problem += 3 * num_trains + 2 * num_planes <= 90

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of trains:", num_trains.value())
print("The number of planes:", num_planes.value())
print("The total profit:", objective.value())
print("## end solving")