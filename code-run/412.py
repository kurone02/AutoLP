from pulp import *

# Define the decision variables
# oil 1 used to produce gas 1
oil_1_gas_1 = LpVariable("Oil1Gas1", lowBound=0, cat='Continuous')
# oil 1 used to produce gas 2
oil_1_gas_2 = LpVariable("Oil1Gas2", lowBound=0, cat='Continuous')
# oil 2 used to produce gas 1
oil_2_gas_1 = LpVariable("Oil2Gas1", lowBound=0, cat='Continuous')
# oil 2 used to produce gas 2
oil_2_gas_2 = LpVariable("Oil2Gas2", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("EuingGasProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 12 * oil_1_gas_1 + 14 * oil_1_gas_2 - (25 * oil_1_gas_1 + 20 * oil_1_gas_2 + 25 * oil_1_gas_2 + 20 * oil_1_gas_2 + 15 * oil_1_gas_2 + 500) - (oil_2_gas_1 + 2 * oil_2_gas_2)
problem += objective

# Define the constraints
# amount of oil 1 used to produce gas 1 and gas 2
problem += oil_1_gas_1 + oil_1_gas_2 <= 500
# amount of oil 2 used to produce gas 1 and gas 2
problem += oil_2_gas_1 + oil_2_gas_2 <= 1000
# Each gallon of gas 1 must contain at least 50 percent oil 1
problem += oil_1_gas_1 >= 0.5 * (oil_1_gas_1 + oil_2_gas_1)
# Each gallon of gas 2 must contain at least 60 percent oil 1
problem += oil_1_gas_2 >= 0.6 * (oil_1_gas_2 + oil_2_gas_2)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of oil 1 purchased:", value(oil_1_gas_1) + value(oil_1_gas_2))
print("The amount of oil 1 used to produce gas 1:", value(oil_1_gas_1))
print("The amount of oil 1 used to produce gas 2:", value(oil_1_gas_2))
print("The amount of oil 2 used to produce gas 1:", value(oil_2_gas_1))
print("The amount of oil 2 used to produce gas 2:", value(oil_2_gas_2))
print("The maximum profit:", value(objective))
print("## end solving")