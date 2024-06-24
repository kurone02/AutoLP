from pulp import *

# Define the decision variables
# number of color printers
num_color_printers = LpVariable("NumColorPrinters", lowBound=0, cat='Integer')
# number of black and white printers
num_bw_printers = LpVariable("NumBWPrinters", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("OfficeSupplyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 200 * num_color_printers + 70 * num_bw_printers
problem += objective

# Define the constraints
# color printer team constraint
problem += num_color_printers <= 20
# black and white printer team constraint
problem += num_bw_printers <= 30
# paper tray installing machine constraint
problem += num_color_printers + num_bw_printers <= 35

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of color printers:", num_color_printers.value())
print("The number of black and white printers:", num_bw_printers.value())
print("The maximum profit:", objective.value())
print("## end solving")