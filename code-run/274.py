from pulp import *

# Define the decision variables
# number of crepe cakes
num_crepe_cakes = LpVariable("NumCrepeCakes", lowBound=0, cat='Integer')
# number of sponge cakes
num_sponge_cakes = LpVariable("NumSpongeCakes", lowBound=0, cat='Integer') 
# number of birthday cakes
num_birthday_cakes = LpVariable("NumBirthdayCakes", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BakeryProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 12 * num_crepe_cakes + 10 * num_sponge_cakes + 15 * num_birthday_cakes
problem += objective

# Define the constraints
# batter constraint
problem += 400 * num_crepe_cakes + 500 * num_sponge_cakes + 450 * num_birthday_cakes <= 20000
# milk constraint
problem += 200 * num_crepe_cakes + 300 * num_sponge_cakes + 350 * num_birthday_cakes <= 14000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of crepe cakes:", num_crepe_cakes.value())
print("The number of sponge cakes:", num_sponge_cakes.value())
print("The number of birthday cakes:", num_birthday_cakes.value())
print("Total profit:", objective.value())
print("## end solving")