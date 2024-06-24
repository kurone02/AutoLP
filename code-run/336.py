from pulp import *

# Define the decision variables
# number of pop concerts
num_pop_concerts = LpVariable("NumPopConcerts", lowBound=0, cat='Integer')
# number of R&B concerts
num_rnb_concerts = LpVariable("NumRnBConcerts", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("SingerConcertProblem", LpMinimize)

# Define the objective function
# minimize the total number of concerts
objective = num_pop_concerts + num_rnb_concerts
problem += objective

# Define the constraints
# total number of audience members
problem += 100 * num_pop_concerts + 240 * num_rnb_concerts >= 10000
# total number of days for practice
problem += 2 * num_pop_concerts + 4 * num_rnb_concerts <= 180
# maximum number of R&B concerts
problem += num_rnb_concerts <= 0.4 * (num_pop_concerts + num_rnb_concerts)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of pop concerts:", num_pop_concerts.value())
print("The number of R&B concerts:", num_rnb_concerts.value())
print("The total number of concerts:", objective.value())
print("## end solving")