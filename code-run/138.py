from pulp import *

# Define the decision variables
# number of kids size bottles
num_kids_bottles = LpVariable("NumKidsBottles", lowBound=50, cat='Integer')
# number of adult size bottles
num_adult_bottles = LpVariable("NumAdultBottles", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CoughSyrupProblem", LpMaximize)

# Define the objective function
# maximize the total number of bottles
objective = num_kids_bottles + num_adult_bottles
problem += objective

# Define the constraints
# total cough syrup available
problem += 100 * num_kids_bottles + 300 * num_adult_bottles <= 25000
# adult size bottle constraint
problem += num_adult_bottles >= 3 * num_kids_bottles
# kids size bottle constraint
problem += num_kids_bottles >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of kids size bottles:", num_kids_bottles.value())
print("The number of adult size bottles:", num_adult_bottles.value())
print("The total number of bottles:", objective.value())
print("## end solving")