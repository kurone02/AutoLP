from pulp import *

# Define the decision variables
# number of commercials during cartoons
num_commercials_cartoon = LpVariable("NumCommercialsCartoon", lowBound=0, cat='Integer')
# number of commercials during kids-movies
num_commercials_kids_movie = LpVariable("NumCommercialsKidsMovie", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ToyCompanyCommercials", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 5000 * num_commercials_cartoon + 12000 * num_commercials_kids_movie
problem += objective

# Define the constraints
# total number of young boys seen
problem += 2 * num_commercials_cartoon + 4 * num_commercials_kids_movie >= 30
# total number of young girls seen
problem += 1 * num_commercials_cartoon + 6 * num_commercials_kids_movie >= 40

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of commercials during cartoons:", num_commercials_cartoon.value())
print("The number of commercials during kids-movies:", num_commercials_kids_movie.value())
print("The total cost of the commercials:", objective.value())
print("## end solving")