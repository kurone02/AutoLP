from pulp import *

# Define the decision variables
# number of salmon meals
num_salmon_meals = LpVariable("NumSalmonMeals", lowBound=0, cat='Integer')
# number of egg meals
num_egg_meals = LpVariable("NumEggMeals", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FitnessGuruMealPlanning", LpMinimize)

# Define the objective function
# minimize the sodium intake
objective = 80 * num_salmon_meals + 20 * num_egg_meals
problem += objective

# Define the constraints
# total calories
problem += 300 * num_salmon_meals + 200 * num_egg_meals >= 2000
# total protein
problem += 15 * num_salmon_meals + 8 * num_egg_meals >= 90
# eggs constraint
problem += num_egg_meals <= 0.4 * (num_salmon_meals + num_egg_meals)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of salmon meals:", num_salmon_meals.value())
print("The number of egg meals:", num_egg_meals.value())
print("The sodium intake (mg):", objective.value())
print("## end solving")