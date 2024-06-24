from pulp import *

# Define the decision variables
oil1_purchased = LpVariable("Oil1Purchased", lowBound=0, cat='Continuous')
oil1_used_gas1 = LpVariable("Oil1UsedGas1", lowBound=0, cat='Continuous')
oil1_used_gas2 = LpVariable("Oil1UsedGas2", lowBound=0, cat='Continuous')
oil2_used_gas1 = LpVariable("Oil2UsedGas1", lowBound=0, cat='Continuous')
oil2_used_gas2 = LpVariable("Oil2UsedGas2", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("EuingGasProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 12 * (oil1_used_gas1 + oil2_used_gas1) + 14 * (oil1_used_gas2 + oil2_used_gas2) - (25 * min(500, oil1_purchased) + 20 * max(0, min(500, oil1_purchased - 500)) + 15 * max(0, min(500, oil1_purchased - 1000)))
problem += objective

# Define the constraints
# total oil 1 available
problem += oil1_purchased + oil1_used_gas1 + oil1_used_gas2 <= 1000
# total oil 2 available
problem += oil2_used_gas1 + oil2_used_gas2 <= 1000
# at least 50% of gas 1 must contain oil 1
problem += oil1_used_gas1 >= 0.5 * (oil1_used_gas1 + oil2_used_gas1)
# at least 60% of gas 2 must contain oil 1
problem += oil1_used_gas2 >= 0.6 * (oil1_used_gas2 + oil2_used_gas2)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of oil 1 purchased:", value(oil1_purchased))
print("The amount of oil 1 used to produce gas 1:", value(oil1_used_gas1))
print("The amount of oil 1 used to produce gas 2:", value(oil1_used_gas2))
print("The amount of oil 2 used to produce gas 1:", value(oil2_used_gas1))
print("The amount of oil 2 used to produce gas 2:", value(oil2_used_gas2))
print("The maximum profit:", value(objective))
print("## end solving")