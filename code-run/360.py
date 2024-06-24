from pulp import *

# Define the decision variables
# number of ambulance shifts
num_ambulance_shifts = LpVariable("NumAmbulanceShifts", lowBound=0, cat='Integer')
# number of van shifts
num_van_shifts = LpVariable("NumVanShifts", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HospitalTransportationProblem", LpMinimize)

# Define the objective function
# minimize the total cost to the hospital
objective = 820 * num_ambulance_shifts + 550 * num_van_shifts
problem += objective

# Define the constraints
# total number of patients to be transported
problem += 20 * num_ambulance_shifts + 15 * num_van_shifts >= 320
# at most 60% of shifts be hospital vans
problem += num_van_shifts <= 0.6 * (num_ambulance_shifts + num_van_shifts)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of ambulance shifts:", num_ambulance_shifts.value())
print("The number of van shifts:", num_van_shifts.value())
print("The total cost to the hospital:", objective.value())
print("## end solving")