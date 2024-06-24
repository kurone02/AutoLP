from pulp import *

# Define the variables
stock1 = LpVariable("Stock1", lowBound=0, cat='Integer')
stock2 = LpVariable("Stock2", lowBound=0, cat='Integer')
stock3 = LpVariable("Stock3", lowBound=0, cat='Integer')
stock4 = LpVariable("Stock4", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("PaperProduction", LpMinimize)
objective = 150 * stock1 + 110 * stock2 + 90 * stock3 + 50 * stock4
problem += objective

# Define the constraints
problem += stock1 + stock2 + stock3 + stock4 == 500
problem += 8 * stock1 + 6 * stock2 + 5 * stock3 + 3 * stock4 >= 7 * 500
problem += 9 * stock1 + 7 * stock2 + 5 * stock3 + 4 * stock4 >= 5 * 500
problem += 8 * stock1 + 5 * stock2 + 6 * stock3 + 5 * stock4 >= 6 * 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The quantity of paper stock 1:", stock1.value())
print("The quantity of paper stock 2:", stock2.value())
print("The quantity of paper stock 3:", stock3.value())
print("The quantity of paper stock 4:", stock4.value())
print("The minimum cost:", objective.value())
print("## end solving")