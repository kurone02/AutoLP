from pulp import *

# Define the decision variables
# number of road bikes
num_road_bikes = LpVariable("NumRoadBikes", lowBound=0, cat='Integer')
# number of mountain bikes
num_mountain_bikes = LpVariable("NumMountainBikes", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BikeFactoryProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 70 * num_road_bikes + 100 * num_mountain_bikes
problem += objective

# Define the constraints
# total tooling time on the grinder
problem += 3 * num_road_bikes + 5 * num_mountain_bikes <= 12
# total tooling time on the polisher
problem += 2 * num_road_bikes + 2.5 * num_mountain_bikes <= 12

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of road bikes produced:", num_road_bikes.value())
print("The number of mountain bikes produced:", num_mountain_bikes.value())
print("The total profit:", objective.value())
print("## end solving")