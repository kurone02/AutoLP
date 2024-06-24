from pulp import *

# Define the decision variables
# number of regular fire fighters
num_regular = LpVariable("RegularFireFighters", lowBound=0, cat='Integer')
# number of emergency fire fighters
num_emergency = LpVariable("EmergencyFireFighters", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FireFighterHiringProblem", LpMinimize)

# Define the objective function
# minimize the total number of fire fighters
problem += num_regular + num_emergency

# Define the constraints
# total hours of fire fighter time
problem += 10 * num_regular + 6 * num_emergency >= 300
# total budget
problem += 300 * num_regular + 100 * num_emergency <= 7000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular fire fighters:", num_regular.value())
print("The number of emergency fire fighters:", num_emergency.value())
print("The total number of fire fighters:", num_regular.value() + num_emergency.value())
print("## end solving")