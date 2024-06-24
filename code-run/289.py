from pulp import *

# Define the decision variables
# number of throwing games
num_throwing_games = LpVariable("NumThrowingGames", lowBound=0, cat='Integer')
# number of climbing games
num_climbing_games = LpVariable("NumClimbingGames", lowBound=5, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("AmusementParkProblem", LpMaximize)

# Define the objective function
# maximize the total number of customers attracted
objective = 15 * num_throwing_games + 8 * num_climbing_games
problem += objective

# Define the constraints
# total cost of prizes per hour
problem += 2 * num_throwing_games + 3 * num_climbing_games <= 100
# throwing games yield more profit than climbing games
problem += num_throwing_games >= 2 * num_climbing_games
# at least 5 games must be climbing
problem += num_climbing_games >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of throwing games:", num_throwing_games.value())
print("The number of climbing games:", num_climbing_games.value())
print("The total number of customers attracted per hour:", objective.value())
print("## end solving")