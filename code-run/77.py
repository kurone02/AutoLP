from pulp import *

# Define the decision variables
num_pills = LpVariable("NumPills", lowBound=0, cat='Integer')
num_cream = LpVariable("NumCream", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PharmacyProfitProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 50 * num_pills + 60 * num_cream
problem += objective

# Define the constraints
# total weighing time
problem += 20 * num_pills + 15 * num_cream <= 4000
# total packaging time
problem += 10 * num_pills + 15 * num_cream <= 3000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of bottles of pills:", num_pills.value())
print("The number of bottles of cream:", num_cream.value())
print("The total profit:", objective.value())
print("## end solving")