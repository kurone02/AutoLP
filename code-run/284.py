from pulp import *

# Define the decision variables
# number of fish meals
num_fish_meals = LpVariable("NumFishMeals", lowBound=0, cat='Integer')
# number of chicken meals
num_chicken_meals = LpVariable("NumChickenMeals", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DietProblem", LpMinimize)

# Define the objective function
# minimize the total fat intake
objective = 7 * num_fish_meals + 10 * num_chicken_meals
problem += objective

# Define the constraints
# protein intake
problem += 10 * num_fish_meals + 15 * num_chicken_meals >= 130
# iron intake
problem += 12 * num_fish_meals + 8 * num_chicken_meals >= 120
# chicken meals are at least twice as many as fish meals
problem += num_chicken_meals >= 2 * num_fish_meals

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of fish meals:", num_fish_meals.value())
print("The number of chicken meals:", num_chicken_meals.value())
print("The total fat intake:", objective.value())
print("## end solving")