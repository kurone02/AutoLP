from pulp import *

# Define the decision variables
# number of burgers
num_burgers = LpVariable("NumBurgers", lowBound=0, cat='Integer')
# number of hot-dogs
num_hot_dogs = LpVariable("NumHotDogs", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MeatFactoryProblem", LpMaximize)

# Define the objective function
# maximize the total revenue
objective = 0.30 * num_burgers + 0.20 * num_hot_dogs
problem += objective

# Define the constraints
# total meat required
problem += 3 * num_burgers + 2 * num_hot_dogs <= 2000
# total binding agent required
problem += 2 * num_burgers + num_hot_dogs <= 1800

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of burgers made:", num_burgers.value())
print("The number of hot-dogs made:", num_hot_dogs.value())
print("The total revenue:", objective.value())
print("## end solving")