from pulp import *

# Define the decision variables
# number of wired headphones
num_wired = LpVariable("NumWired", lowBound=0, cat='Integer')
# number of wireless headphones
num_wireless = LpVariable("NumWireless", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HeadphoneProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 50 * num_wired + 20 * num_wireless
problem += objective

# Define the constraints
# wired team constraint
problem += num_wired <= 100
# wireless team constraint
problem += num_wireless <= 170
# audio testing machine constraint
problem += num_wired + num_wireless <= 150

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of wired headphones:", num_wired.value())
print("The number of wireless headphones:", num_wireless.value())
print("Total profit:", objective.value())
print("## end solving")