from pulp import *

# Define the decision variables
num_gas_grills = LpVariable("NumGasGrills", lowBound=0, cat='Integer')
num_electric_grills = LpVariable("NumElectricGrills", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("BurgerChainProblem", LpMinimize)

# Define the objective function
# minimize the total number of grills
objective = num_gas_grills + num_electric_grills
problem += objective

# Define the constraints
# minimum number of patties
problem += 20 * num_gas_grills + 30 * num_electric_grills >= 150
# maximum amount of cooking oil
problem += 20 * num_gas_grills + 25 * num_electric_grills <= 140
# electric grills must be less than gas grills
problem += num_electric_grills <= num_gas_grills

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of gas grills:", num_gas_grills.value())
print("The number of electric grills:", num_electric_grills.value())
print("Total number of grills in the store:", objective.value())
print("## end solving")