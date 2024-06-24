from pulp import *

# Define the decision variables
# number of original meals
num_original_meals = LpVariable("NumOriginalMeals", lowBound=0, cat='Integer')
# number of experimental meals
num_experimental_meals = LpVariable("NumExperimentalMeals", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("RestaurantProblem", LpMinimize)

# Define the objective function
# minimize the total cooking time
objective = 10 * num_original_meals + 15 * num_experimental_meals
problem += objective

# Define the constraints
# total wrapping waste
problem += 45 * num_original_meals + 35 * num_experimental_meals <= 900
# total food waste
problem += 20 * num_original_meals + 25 * num_experimental_meals <= 800

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of original meals:", num_original_meals.value())
print("The number of experimental meals:", num_experimental_meals.value())
print("The total cooking time:", objective.value())
print("## end solving")