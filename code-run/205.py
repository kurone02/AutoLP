from pulp import *

# Define the decision variables
# number of beam bridges
num_beam_bridges = LpVariable("NumBeamBridges", lowBound=0, cat='Integer')
# number of truss bridges
num_truss_bridges = LpVariable("NumTrussBridges", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BridgeBuildingProblem", LpMaximize)

# Define the objective function
# maximize the total mass that can be supported
objective = 40 * num_beam_bridges + 60 * num_truss_bridges
problem += objective

# Define the constraints
# total Popsicle sticks
problem += 30 * num_beam_bridges + 50 * num_truss_bridges <= 600
# total glue
problem += 5 * num_beam_bridges + 8 * num_truss_bridges <= 100
# number of truss bridges
problem += num_truss_bridges <= 5
# number of beam bridges
problem += num_beam_bridges >= num_truss_bridges

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of beam bridges:", num_beam_bridges.value())
print("The number of truss bridges:", num_truss_bridges.value())
print("The total mass that can be supported:", objective.value())
print("## end solving")