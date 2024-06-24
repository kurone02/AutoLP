from pulp import *

# Define the decision variables
# number of type 1 circuits to produce
num_circuit_type1 = LpVariable("NumCircuitType1", lowBound=0, cat='Integer')
# number of type 2 circuits to produce
num_circuit_type2 = LpVariable("NumCircuitType2", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ElectronicComponentProductionProblem", LpMaximize)

# Define the objective function
# maximize the total financial returns
objective = 5 * num_circuit_type1 + 12 * num_circuit_type2
problem += objective

# Define the constraints
# component A constraint
problem += 20 * num_circuit_type1 + 10 * num_circuit_type2 <= 200
# component B constraint
problem += 10 * num_circuit_type1 + 20 * num_circuit_type2 <= 120
# component C constraint
problem += 10 * num_circuit_type1 + 30 * num_circuit_type2 <= 150

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of type 1 circuits to produce:", num_circuit_type1.value())
print("The number of type 2 circuits to produce:", num_circuit_type2.value())
print("The maximum financial returns:", objective.value())
print("## end solving")