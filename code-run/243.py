from pulp import *

# Define the decision variables
# number of labradors
num_labradors = LpVariable("NumLabradors", lowBound=0, cat='Integer')
# number of golden retrievers
num_golden_retrievers = LpVariable("NumGoldenRetrievers", lowBound=50, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DogSchoolProblem", LpMaximize)

# Define the objective function
# maximize the total number of newspapers delivered
objective = 7 * num_labradors + 10 * num_golden_retrievers
problem += objective

# Define the constraints
# small bone treats available
problem += 5 * num_labradors + 6 * num_golden_retrievers <= 1500
# minimum golden retrievers
# already defined as a constraint
# maximum percentage of labradors
problem += num_labradors <= 0.6 * (num_labradors + num_golden_retrievers)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of labradors:", num_labradors.value())
print("The number of golden retrievers:", num_golden_retrievers.value())
print("The number of newspapers delivered:", objective.value())
print("## end solving")