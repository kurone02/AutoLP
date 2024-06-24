from pulp import *

# Define the decision variables
oil1 = LpVariable("Oil1", lowBound=0, cat='Continuous')
oil1_gas1 = LpVariable("Oil1Gas1", lowBound=0, cat='Continuous')
oil1_gas2 = LpVariable("Oil1Gas2", lowBound=0, cat='Continuous')
oil2_gas1 = LpVariable("Oil2Gas1", lowBound=0, cat='Continuous')
oil2_gas2 = LpVariable("Oil2Gas2", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("EuingGasProblem", LpMaximize)

# Define the objective function
objective = 12 * oil1_gas1 + 14 * oil1_gas2 - 25 * min(oil1, 500) - 20 * max(0, oil1 - 500) - 15 * max(0, oil1 - 1000)
problem += objective

# Define the constraints
problem += oil1_gas1 + oil1_gas2 <= 500
problem += oil1_gas1 >= 0.5 * oil1
problem += oil1_gas2 >= 0.6 * oil1
problem += oil2_gas1 <= 1000
problem += oil2_gas2 <= 1000
problem += oil1 + oil2 <= 1500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of oil 1 purchased:", oil1.value())
print("The amount of oil 1 used to produce gas 1:", oil1_gas1.value())
print("The amount of oil 1 used to produce gas 2:", oil1_gas2.value())
print("The amount of oil 2 used to produce gas 1:", oil2_gas1.value())
print("The amount of oil 2 used to produce gas 2:", oil2_gas2.value())
print("The maximum profit:", objective.value())
print("## end solving")