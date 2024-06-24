from pulp import *

# Define the variables
num_large_pizzas = LpVariable("NumLargePizzas", lowBound=0, cat='Integer')
num_medium_pizzas = LpVariable("NumMediumPizzas", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PizzaRestaurantProblem", LpMinimize)

# Define the objective function
problem += 12 * num_large_pizzas + 8 * num_medium_pizzas

# Define the constraints
problem += 12 * num_large_pizzas + 8 * num_medium_pizzas <= 10000
problem += 5 * num_large_pizzas + 4 * num_medium_pizzas <= 4400
problem += num_medium_pizzas >= 200
problem += num_large_pizzas >= 2 * num_medium_pizzas

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of large pizzas to make:", num_large_pizzas.value())
print("The number of medium pizzas to make:", num_medium_pizzas.value())
print("The total time spent baking:", problem.objective.value())
print("## end solving")