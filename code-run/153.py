from pulp import *

# Define the decision variables
# number of compact cars
num_compact_cars = LpVariable("NumCompactCars", lowBound=1000, cat='Integer')
# number of midsize cars
num_midsize_cars = LpVariable("NumMidsizeCars", lowBound=1000, cat='Integer') 
# number of large cars
num_large_cars = LpVariable("NumLargeCars", lowBound=1000, cat='Integer') 

# Define the question as a maximum problem
problem = LpProblem("DorianAutoProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 2000 * num_compact_cars + 3000 * num_midsize_cars + 4000 * num_large_cars
problem += objective

# Define the constraints
# total steel required
problem += 1.5 * num_compact_cars + 3 * num_midsize_cars + 5 * num_large_cars <= 10000
# total labor required
problem += 30 * num_compact_cars + 40 * num_midsize_cars + 25 * num_large_cars <= 120000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of compact cars to produce:", num_compact_cars.value())
print("The number of midsize cars to produce:", num_midsize_cars.value())
print("The number of large cars to produce:", num_large_cars.value())
print("The maximum profit:", objective.value())
print("## end solving")