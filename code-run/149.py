from pulp import *

# Define the decision variables
# number of waiters
num_waiters = LpVariable("NumWaiters", lowBound=0, cat='Integer')
# number of managers
num_managers = LpVariable("NumManagers", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("RestaurantProblem", LpMinimize)

# Define the objective function
# minimize the total wage bill
objective = 1200 * num_waiters + 2000 * num_managers
problem += objective

# Define the constraints
# managers as a third of the waiters
problem  += 3*num_managers >= num_waiters # problem += num_managers >= 1/3 * num_waiters
# minimum number of workers
problem += num_waiters + num_managers >= 50
# at least 15 managers
problem += num_managers >= 15
# total wage bill
problem += 1200 * num_waiters + 2000 * num_managers <= 500000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of waiters:", num_waiters.value())
print("The number of managers:", num_managers.value())
print("The total wage bill:", objective.value())
print("## end solving")