from pulp import *

# Define the decision variables
# number of sofas to produce
num_sofas = LpVariable("NumSofas", lowBound=0, cat='Integer')
# number of kitchen cabinets to produce
num_cabinets = LpVariable("NumCabinets", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("EastOakDesignsProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 400 * num_sofas + 1200 * num_cabinets
problem += objective

# Define the constraints
# lacquer constraint
problem += 3 * num_sofas + 10 * num_cabinets <= 100
# oak constraint
problem += 10 * num_sofas + 24 * num_cabinets <= 300

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of sofas to produce:", num_sofas.value())
print("The number of kitchen cabinets to produce:", num_cabinets.value())
print("The maximum profit:", objective.value())
print("## end solving")