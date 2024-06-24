from pulp import *

# Define the decision variables
num_circuit1 = LpVariable("NumCircuit1", lowBound=0, cat='Integer')
num_circuit2 = LpVariable("NumCircuit2", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CircuitProductionProblem", LpMaximize)

# Define the objective function
objective = 5 * num_circuit1 + 12 * num_circuit2
problem += objective

# Define the constraints
problem += 20 * num_circuit1 + 10 * num_circuit2 <= 200
problem += 10 * num_circuit1 + 20 * num_circuit2 <= 120
problem += 10 * num_circuit1 + 30 * num_circuit2 <= 150

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of type 1 circuits to produce:", num_circuit1.value())
print("The number of type 2 circuits to produce:", num_circuit2.value())
print("The maximum financial returns:", objective.value())
print("## end solving")