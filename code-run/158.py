from pulp import *

# Define the variables
q_fertilizer1 = LpVariable("q_fertilizer1", lowBound=0, cat='Continuous')
q_fertilizer2 = LpVariable("q_fertilizer2", lowBound=0, cat='Continuous')
q_fertilizer3 = LpVariable("q_fertilizer3", lowBound=0, cat='Continuous')
q_fertilizer4 = LpVariable("q_fertilizer4", lowBound=0, cat='Continuous')
q_fertilizer5 = LpVariable("q_fertilizer5", lowBound=0, cat='Continuous')

# Define the objective function
problem = LpProblem("FertilizerProblem", LpMinimize)
objective = 21.75 * q_fertilizer1 + 23.75 * q_fertilizer2 + 22.00 * q_fertilizer3 + 19.50 * q_fertilizer4 + 18.50 * q_fertilizer5
problem += objective

# Define the constraints
problem += 10 * q_fertilizer1 + 8 * q_fertilizer2 + 12 * q_fertilizer3 + 10 * q_fertilizer4 + 15 * q_fertilizer5 >= 1000
problem += 10 * q_fertilizer1 + 8 * q_fertilizer2 + 12 * q_fertilizer3 + 10 * q_fertilizer4 + 15 * q_fertilizer5 <= 1050
problem += 8 * q_fertilizer1 + 11 * q_fertilizer2 + 7 * q_fertilizer3 + 10 * q_fertilizer4 + 10 * q_fertilizer5 >= 800
problem += 8 * q_fertilizer1 + 11 * q_fertilizer2 + 7 * q_fertilizer3 + 10 * q_fertilizer4 + 10 * q_fertilizer5 <= 850
problem += 12 * q_fertilizer1 + 15 * q_fertilizer2 + 12 * q_fertilizer3 + 10 * q_fertilizer4 + 6 * q_fertilizer5 >= 1200
problem += 12 * q_fertilizer1 + 15 * q_fertilizer2 + 12 * q_fertilizer3 + 10 * q_fertilizer4 + 6 * q_fertilizer5 <= 1250
problem += q_fertilizer1 + q_fertilizer2 + q_fertilizer3 + q_fertilizer4 + q_fertilizer5 <= 10000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The quantity of Fertilizer 1:", q_fertilizer1.value())
print("The quantity of Fertilizer 2:", q_fertilizer2.value())
print("The quantity of Fertilizer 3:", q_fertilizer3.value())
print("The quantity of Fertilizer 4:", q_fertilizer4.value())
print("The quantity of Fertilizer 5:", q_fertilizer5.value())
print("## end solving")