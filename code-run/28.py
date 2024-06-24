from pulp import *

# Define the variables
num_coffees = LpVariable("NumCoffees", lowBound=0, cat='Integer')
num_hot_chocolates = LpVariable("NumHotChocolates", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("IceHockeyProblem", LpMaximize)
objective = 0.22 * num_coffees + 0.14 * num_hot_chocolates
problem += objective

# Define the constraints
problem += num_coffees >= 40
problem += num_hot_chocolates >= 20
problem += num_coffees <= 60
problem += num_hot_chocolates <= 35
problem += num_coffees + num_hot_chocolates <= 75

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of coffees sold:", value(num_coffees))
print("The number of hot chocolates sold:", value(num_hot_chocolates))
print("The total profit:", value(objective))
print("## end solving")