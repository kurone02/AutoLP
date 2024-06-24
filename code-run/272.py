from pulp import *

# Define the decision variables
# number of peach candy packs
num_peach_candy = LpVariable("NumPeachCandy", lowBound=0, cat='Integer')
# number of cherry candy packs
num_cherry_candy = LpVariable("NumCherryCandy", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CandyProblem", LpMinimize)

# Define the objective function
# minimize the total amount of special syrup used
objective = 5 * num_peach_candy + 4 * num_cherry_candy
problem += objective

# Define the constraints
# peach flavoring
problem += 3 * num_peach_candy + 5 * num_cherry_candy <= 3000
# cherry flavoring
problem += 5 * num_peach_candy + 4 * num_cherry_candy <= 4000
# more peach than cherry
problem += num_peach_candy >= num_cherry_candy
# at least 30% of the pack must be cherry flavored
problem += num_cherry_candy >= 0.3 * (num_peach_candy + num_cherry_candy)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of peach candy packs:", num_peach_candy.value())
print("The number of cherry candy packs:", num_cherry_candy.value())
print("The total amount of special syrup used:", objective.value())
print("## end solving")