from pulp import *

# Define the decision variables
num_type_A = LpVariable("NumTypeA", lowBound=0, cat='Integer')
num_type_B = LpVariable("NumTypeB", lowBound=0, cat='Integer') 
num_type_C = LpVariable("NumTypeC", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("LandscaperProblem", LpMaximize)

# Define the objective function
objective = 200 * num_type_A + 175 * num_type_B + 225 * num_type_C
problem += objective

# Define the constraints
problem += 10 * num_type_A + 5 * num_type_B + 12 * num_type_C <= 1200
problem += 7 * num_type_A + 12 * num_type_B + 4 * num_type_C <= 700
problem += 15 * num_type_A + 10 * num_type_B + 12 * num_type_C <= 2000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of type A layouts:", num_type_A.value())
print("The number of type B layouts:", num_type_B.value())
print("The number of type C layouts:", num_type_C.value())
print("Total profit:", objective.value())
print("## end solving")