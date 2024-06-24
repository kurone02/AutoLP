from pulp import *

# Define the decision variables
# amount of oil 1 purchased
oil_1_purchased = LpVariable("Oil1Purchased", lowBound=0, cat='Continuous')
# amount of oil 1 used to produce gas 1
oil_1_gas_1 = LpVariable("Oil1Gas1", lowBound=0, cat='Continuous')
# amount of oil 1 used to produce gas 2
oil_1_gas_2 = LpVariable("Oil1Gas2", lowBound=0, cat='Continuous')
# amount of oil 2 used to produce gas 1
oil_2_gas_1 = LpVariable("Oil2Gas1", lowBound=0, cat='Continuous')
# amount of oil 2 used to produce gas 2
oil_2_gas_2 = LpVariable("Oil2Gas2", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("EuingGasProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 12 * oil_1_gas_1 + 14 * oil_1_gas_2 - (25 * min(oil_1_purchased, 500) + 20 * min(max(oil_1_purchased - 500, 0), 500) + 15 * max(oil_1_purchased - 1000, 0))
problem += objective

# Define the constraints
# amount of oil 1 used to produce gas 1 and gas 2
problem += oil_1_gas_1 + oil_1_gas_2 <= oil_1_purchased
# amount of oil 2 used to produce gas 1 and gas 2
problem += oil_2_gas_1 + oil_2_gas_2 <= 1000
# amount of oil 1 used to produce gas 1
problem += oil_1_gas_1 + 0.5 * (oil_1_gas_1 + oil_2_gas_1) >= 0.5 * (oil_1_gas_1 + oil_2_gas_1 + oil_1_gas_2 + oil_2_gas_2)
# amount of oil 1 used to produce gas 2
problem += oil_1_gas_2 + 0.6 * (oil_1_gas_2 + oil_2_gas_2) >= 0.6 * (oil_1_gas_1 + oil_2_gas_1 + oil_1_gas_2 + oil_2_gas_2)
# total amount of oil 1 used
problem += oil_1_gas_1 + oil_1_gas_2 + oil_2_gas_1 + oil_2_gas_2 <= 500 + 1000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of oil 1 purchased:", oil_1_purchased.value())
print("The amount of oil 1 used to produce gas 1:", oil_1_gas_1.value())
print("The amount of oil 1 used to produce gas 2:", oil_1_gas_2.value())
print("The amount of oil 2 used to produce gas 1:", oil_2_gas_1.value())
print("The amount of oil 2 used to produce gas 2:", oil_2_gas_2.value())
print("The maximum profit:", objective.value())
print("## end solving")