from pulp import *

# Define the decision variables
grain_A = LpVariable("GrainA", lowBound=0, cat='Continuous')
grain_B = LpVariable("GrainB", lowBound=0, cat='Continuous')
grain_C = LpVariable("GrainC", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("WoolCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 41 * grain_A + 36 * grain_B + 96 * grain_C
problem += objective

# Define the constraints
# nutrient A constraint
problem += grain_A * 20 + grain_B * 10 + grain_C * 50 >= 70
# nutrient B constraint
problem += grain_A * 30 + grain_B * 10 + grain_C * 30 >= 10
# nutrient C constraint
problem += grain_A * 70 + grain_B * 0 + grain_C * 0 >= 0
# nutrient D constraint
problem += grain_A * 110 + grain_B * 18 + grain_C * 90 >= 10

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of grain A to feed the sheep:", value(grain_A))
print("The amount of grain B to feed the sheep:", value(grain_B))
print("The amount of grain C to feed the sheep:", value(grain_C))
print("The minimum cost:", value(objective))
print("## end solving")