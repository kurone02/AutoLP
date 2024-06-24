from pulp import *

# Define the decision variables
# number of painkiller pills
num_painkillers = LpVariable("NumPainkillers", lowBound=50, cat='Integer')
# number of sleeping pills
num_sleeping_pills = LpVariable("NumSleepingPills", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PharmacyProblem", LpMinimize)

# Define the objective function
# minimize the total amount of digestive medicine needed
objective = 3 * num_painkillers + 5 * num_sleeping_pills
problem += objective

# Define the constraints
# total amount of morphine
problem += 10 * num_painkillers + 6 * num_sleeping_pills <= 3000
# minimum painkiller pills
problem += num_painkillers >= 50
# sleeping pills popularity
problem += num_sleeping_pills >= 0.7 * (num_painkillers + num_sleeping_pills)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of painkiller pills:", num_painkillers.value())
print("The number of sleeping pills:", num_sleeping_pills.value())
print("The total amount of digestive medicine needed:", objective.value())
print("## end solving")