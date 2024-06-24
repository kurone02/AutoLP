from pulp import *

# Define the variables
num_glasses_milk = LpVariable("NumGlassesMilk", lowBound=0, cat='Integer')
num_plates_vegetables = LpVariable("NumPlatesVegetables", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("GrowthOptimization", LpMinimize)
objective = 1 * num_glasses_milk + 2 * num_plates_vegetables
problem += objective

# Define the constraints
problem += 40 * num_glasses_milk + 15 * num_plates_vegetables >= 100
problem += 25 * num_glasses_milk + 30 * num_plates_vegetables >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of glasses of milk:", value(num_glasses_milk))
print("The number of plates of vegetables:", value(num_plates_vegetables))
print("Total cost:", value(objective))
print("## end solving")