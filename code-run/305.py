from pulp import *

# Define the decision variables
# number of small packets
num_packets = LpVariable("NumPackets", lowBound=3, cat='Integer')
# number of jugs
num_jugs = LpVariable("NumJugs", lowBound=3*num_packets.value(), cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("JamBusinessProblem", LpMaximize)

# Define the objective function
# maximize the total number of units that can be sold
objective = num_packets + num_jugs
problem += objective

# Define the constraints
# total amount of jam
problem += 1000 * num_packets + 1250 * num_jugs <= 65000
# at least three times as many jugs as sets of small packets
problem += num_jugs >= 3 * num_packets
# at least 3 sets of small packets
problem += num_packets >= 3

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small packets:", num_packets.value())
print("The number of jugs:", num_jugs.value())
print("The total number of units that can be sold:", objective.value())
print("## end solving")