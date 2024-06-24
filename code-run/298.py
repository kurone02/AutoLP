from pulp import *

# Define the decision variables
# number of prevention pills
num_preventive_pills = LpVariable("NumPreventivePills", lowBound=0, cat='Integer')
# number of treatment pills
num_treatment_pills = LpVariable("NumTreatmentPills", lowBound=50, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HospitalPillsProblem", LpMaximize)

# Define the objective function
# maximize the total number of patients that can be treated
objective = num_preventive_pills + num_treatment_pills
problem += objective

# Define the constraints
# total cost of making the pills
problem += 15 * num_preventive_pills + 25 * num_treatment_pills <= 10000
# at least 2 times as many prevention pills as treatment pills
problem += num_preventive_pills >= 2 * num_treatment_pills
# at least 50 treatment pills
problem += num_treatment_pills >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of prevention pills:", num_preventive_pills.value())
print("The number of treatment pills:", num_treatment_pills.value())
print("The total number of patients that can be treated:", objective.value())
print("## end solving")