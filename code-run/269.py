from pulp import *

# Define the decision variables
# number of laminate planks
num_laminate_planks = LpVariable("NumLaminatePlanks", lowBound=15000, upBound=40000, cat='Integer')
# number of carpets
num_carpets = LpVariable("NumCarpets", lowBound=5000, upBound=20000, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FlooringCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 2.1 * num_laminate_planks + 3.3 * num_carpets
problem += objective

# Define the constraints
# total production
problem += num_laminate_planks + num_carpets <= 50000
# minimum demand for laminate planks
problem += num_laminate_planks >= 15000
# minimum demand for carpets
problem += num_carpets >= 5000
# limit on laminate planks production
problem += num_laminate_planks <= 40000
# limit on carpets production
problem += num_carpets <= 20000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of laminate planks to be made weekly (in square feet):", num_laminate_planks.value())
print("The amount of carpets to be made weekly (in square feet):", num_carpets.value())
print("The total profit:", objective.value())
print("## end solving")