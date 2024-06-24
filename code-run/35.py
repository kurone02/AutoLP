from pulp import *

# Define the decision variables
# number of solar calculators
num_solar_calcs = LpVariable("NumSolarCalcs", lowBound=0, cat='Integer')
# number of finance calculators
num_finance_calcs = LpVariable("NumFinanceCalcs", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ElectronicsFactoryProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 12 * num_solar_calcs + 9 * num_finance_calcs
problem += objective

# Define the constraints
# total silicon
problem += 5 * num_solar_calcs + 3 * num_finance_calcs <= 150
# total plastic
problem += 4 * num_solar_calcs + 5 * num_finance_calcs <= 150
# total steel
problem += 2 * num_solar_calcs + 3 * num_finance_calcs <= 70

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of solar calculators produced:", num_solar_calcs.value())
print("The number of finance calculators produced:", num_finance_calcs.value())
print("The maximum profit:", objective.value())
print("## end solving")