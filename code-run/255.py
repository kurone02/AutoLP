from pulp import *

# Define the decision variables
# number of canoes needed
num_canoes = LpVariable("NumCanoes", lowBound=0, cat='Integer')
# number of diesel boats needed
num_diesel_boats = LpVariable("NumDieselBoats", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FishingBoatProblem", LpMinimize)

# Define the objective function
objective = num_canoes + num_diesel_boats
# minimize the total number of canoes and diesel boats needed
problem += objective

# Define the constraints
# at least 1000 fish need to be transported to shore
problem += 10 * num_canoes + 15 * num_diesel_boats >= 1000
# the number of small canoes used has to be at least 3 times as many as the number of diesel boats uses
problem += num_canoes >= 3 * num_diesel_boats

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of canoes:", num_canoes.value())
print("The number of diesel boats:", num_diesel_boats.value())
print("The total number of boats used:", objective.value())
print("## end solving")