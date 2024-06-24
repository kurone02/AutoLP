from pulp import *

# Define the decision variables
carrot_kg = LpVariable("CarrotKg", lowBound=0, cat='Continuous')
cabbage_kg = LpVariable("CabbageKg", lowBound=0, cat='Continuous')
cucumber_kg = LpVariable("CucumberKg", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("NutritionProblem", LpMinimize)
objective = 0.75 * carrot_kg + 0.5 * cabbage_kg + 0.15 * cucumber_kg
problem += objective

# Define the constraints
problem += 0.5 * carrot_kg + 0.5 * cucumber_kg >= 0.5
problem += 35 * carrot_kg + 300 * cabbage_kg + 10 * cucumber_kg >= 15
problem += 30 * carrot_kg + 20 * cabbage_kg + 10 * cucumber_kg >= 4
problem += carrot_kg + cabbage_kg + cucumber_kg <= 1

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of carrot (kg) to be added to each dish:", value(carrot_kg))
print("The amount of white cabbage (kg) to be added to each dish:", value(cabbage_kg))
print("The amount of cucumber (kg) to be added to each dish:", value(cucumber_kg))
print("The minimum additional price per dish:", value(objective))
print("## end solving")