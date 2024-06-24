from pulp import *

# Define the decision variables
# number of experiment 1 conducted
num_experiment1 = LpVariable("NumExperiment1", lowBound=0, cat='Integer')
# number of experiment 2 conducted
num_experiment2 = LpVariable("NumExperiment2", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ChemistryProblem", LpMaximize)

# Define the objective function
# maximize the total amount of green gas produced
objective = 5 * num_experiment1 + 6 * num_experiment2
problem += objective

# Define the constraints
# total red liquid available
problem += 3 * num_experiment1 + 5 * num_experiment2 <= 80
# total blue liquid available
problem += 4 * num_experiment1 + 3 * num_experiment2 <= 70
# total smelly gas produced
problem += num_experiment1 + 2 * num_experiment2 <= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of Experiment 1 conducted:", num_experiment1.value())
print("The number of Experiment 2 conducted:", num_experiment2.value())
print("The total units of green gas produced:", objective.value())
print("## end solving")