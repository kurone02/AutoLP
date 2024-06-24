from pulp import *

# Define the decision variables
# number of matcha ice cream
num_matcha = LpVariable("NumMatcha", lowBound=0, cat='Integer')
# number of orange sorbet
num_sorbet = LpVariable("NumSorbet", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DessertShopProblem", LpMinimize)

# Define the objective function
# minimize the total amount of flavouring needed
objective = 4 * num_matcha + 3 * num_sorbet
problem += objective

# Define the constraints
# ice cream constraint
problem += num_matcha + 4 * num_sorbet <= 600
# water constraint
problem += 4 * num_matcha + num_sorbet <= 550
# at least fifteen percent of desserts must be matcha ice cream
problem += num_matcha >= 0.15 * (num_matcha + num_sorbet)
# more orange sorbet should be made than matcha ice cream
problem += num_sorbet >= num_matcha

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of matcha ice cream:", num_matcha.value())
print("The number of orange sorbet:", num_sorbet.value())
print("The total amount of flavoring needed:", objective.value())
print("## end solving")