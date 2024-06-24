from pulp import *

# Define the decision variables
# number of seasonal volunteers
num_seasonal_volunteers = LpVariable("NumSeasonalVolunteers", lowBound=0, cat='Integer')
# number of full-time volunteers
num_fulltime_volunteers = LpVariable("NumFulltimeVolunteers", lowBound=10, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ToyStoreVolunteerProblem", LpMaximize)

# Define the objective function
# maximize the total number of gifts that can be delivered
objective = 5 * num_seasonal_volunteers + 8 * num_fulltime_volunteers
problem += objective

# Define the constraints
# total points
problem += 2 * num_seasonal_volunteers + 5 * num_fulltime_volunteers <= 200
# maximum 30% of volunteers can be seasonal
problem += num_seasonal_volunteers <= 0.3 * (num_seasonal_volunteers + num_fulltime_volunteers)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of seasonal volunteers:", num_seasonal_volunteers.value())
print("The number of full-time volunteers:", num_fulltime_volunteers.value())
print("The total number of gifts delivered:", objective.value())
print("## end solving")