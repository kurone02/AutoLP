from pulp import *

# Define the decision variables
num_small_teams = LpVariable("NumSmallTeams", lowBound=0, cat='Integer')
num_large_teams = LpVariable("NumLargeTeams", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("LawnMowingProblem", LpMaximize)

# Define the objective function
# maximize the total lawn that can be mowed
objective = 50 * num_small_teams + 80 * num_large_teams
problem += objective

# Define the constraints
# total number of employees
problem += 3 * num_small_teams + 5 * num_large_teams <= 150
# number of small teams is at least 3 times as much as the number of large teams
problem += num_small_teams >= 3 * num_large_teams
# there has to be at least 6 large teams
problem += num_large_teams >= 6
# there has to be at least 10 small teams
problem += num_small_teams >= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small teams:", num_small_teams.value())
print("The number of large teams:", num_large_teams.value())
print("The total amount of lawn that can be mowed:", objective.value())
print("## end solving")