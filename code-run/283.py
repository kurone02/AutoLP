from pulp import *

# Define the decision variables
# hours of machine 1
hours_machine1 = LpVariable("HoursMachine1", lowBound=0, cat='Continuous')
# hours of machine 2
hours_machine2 = LpVariable("HoursMachine2", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PharmacyProblem", LpMinimize)

# Define the objective function
# minimize the total time
objective = hours_machine1 + hours_machine2
problem += objective

# Define the constraints
# total eye cream and foot cream
problem += 30 * hours_machine1 + 45 * hours_machine2 >= 1300
problem += 60 * hours_machine1 + 30 * hours_machine2 >= 1500
# total distilled water
problem += 20 * hours_machine1 + 15 * hours_machine2 <= 1200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The hours machine 1 should be used:", hours_machine1.value())
print("The hours machine 2 should be used:", hours_machine2.value())
print("The total time needed:", objective.value())
print("## end solving")