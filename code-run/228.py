from pulp import *

# Define the decision variables
num_small_suitcases = LpVariable("NumSmallSuitcases", lowBound=0, cat='Integer')
num_large_suitcases = LpVariable("NumLargeSuitcases", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SnackExporterProblem", LpMaximize)

# Define the objective function
# maximize the total number of snacks that can be delivered
objective = 50 * num_small_suitcases + 80 * num_large_suitcases
problem += objective

# Define the constraints
# at least twice as many small suitcases must be used as large suitcases
problem += num_small_suitcases >= 2 * num_large_suitcases
# at least 15 large suitcases must be used
problem += num_large_suitcases >= 15
# at most 70 small suitcases can be used
problem += num_small_suitcases <= 70
# at most 50 large suitcases can be used
problem += num_large_suitcases <= 50
# at most 70 suitcases can be used in total
problem += num_small_suitcases + num_large_suitcases <= 70

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small suitcases:", num_small_suitcases.value())
print("The number of large suitcases:", num_large_suitcases.value())
print("The total number of snacks transported:", objective.value())
print("## end solving")