from pulp import *

# Define the variables
carrots = LpVariable("Carrots", lowBound=0, cat='Continuous')
cabbage = LpVariable("Cabbage", lowBound=0, cat='Continuous')
cucumber = LpVariable("Cucumber", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("NutritionProblem", LpMinimize)
objective = 0.75 * carrots + 0.5 * cabbage + 0.15 * cucumber
problem += objective

# Define the constraints
problem += 0.5 * 0.5 + 0.5 * 300 + 0.5 * 0.5 >= 35 * carrots + 0.5 * cabbage + 4 * cucumber
problem += 0.5 * 60 + 0.5 * 300 + 0.5 * 10 >= 35 * carrots + 0.5 * cabbage + 4 * cucumber
problem += 0.5 * 30 + 0.5 * 20 + 0.5 * 10 >= 35 * carrots + 0.5 * cabbage + 4 * cucumber

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of carrot (kg) to be added to each dish:", value(carrots))
print("The amount of white cabbage (kg) to be added to each dish:", value(cabbage))
print("The amount of cucumber (kg) to be added to each dish:", value(cucumber))
print("The minimum additional price per dish:", value(objective))
print("## end solving")