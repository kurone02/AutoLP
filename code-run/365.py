from pulp import *

# Define the decision variables
num_workers_shift1 = LpVariable("NumWorkersShift1", lowBound=0, cat='Integer')
num_workers_shift2 = LpVariable("NumWorkersShift2", lowBound=0, cat='Integer')
num_workers_shift3 = LpVariable("NumWorkersShift3", lowBound=0, cat='Integer')
num_workers_shift4 = LpVariable("NumWorkersShift4", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("StaffSchedulingProblem", LpMinimize)

# Define the objective function
objective = 135 * num_workers_shift1 + 140 * num_workers_shift2 + 190 * num_workers_shift3 + 188 * num_workers_shift4
problem += objective

# Define the constraints
problem += num_workers_shift1 >= 55
problem += num_workers_shift2 >= 46
problem += num_workers_shift3 >= 59
problem += num_workers_shift4 >= 23
problem += num_workers_shift1 >= 20
problem += num_workers_shift2 >= 30
problem += num_workers_shift3 >= 38
problem += num_workers_shift4 >= 60

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of workers for shift 1:", num_workers_shift1.value())
print("The number of workers for shift 2:", num_workers_shift2.value())
print("The number of workers for shift 3:", num_workers_shift3.value())
print("The number of workers for shift 4:", num_workers_shift4.value())
print("The total wage cost:", objective.value())
print("## end solving")