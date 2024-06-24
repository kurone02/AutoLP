from pulp import *

# Define the decision variables
# number of square feet of hardwood produced weekly
num_hardwood = LpVariable("NumHardwood", lowBound=20000, upBound=50000, cat='Continuous')
# number of square feet of vinyl produced weekly
num_vinyl = LpVariable("NumVinyl", lowBound=10000, upBound=30000, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FlooringCompanyProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 2.5 * num_hardwood + 3 * num_vinyl
problem += objective

# Define the constraints
# total amount of flooring produced weekly
problem += num_hardwood + num_vinyl >= 60000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of square feet of hardwood flooring produced weekly:", num_hardwood.value())
print("The number of square feet of vinyl planks produced weekly:", num_vinyl.value())
print("The maximum company's profit:", objective.value())
print("## end solving")