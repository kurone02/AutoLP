from pulp import *

# Define the decision variables
# amount invested in condos
amount_invested_in_condos = LpVariable("AmountInvestedInCondos", lowBound=0, cat='Continuous')
# amount invested in detached houses
amount_invested_in_detached_houses = LpVariable("AmountInvestedInDetachedHouses", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("MrsWatsonInvestmentProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.5 * amount_invested_in_condos + 1 * amount_invested_in_detached_houses
problem += objective

# Define the constraints
# total investment
problem += amount_invested_in_condos + amount_invested_in_detached_houses <= 760000
# minimum 20% in condos
problem += amount_invested_in_condos >= 0.20 * (amount_invested_in_condos + amount_invested_in_detached_houses)
# at least $20000 in detached houses
problem += amount_invested_in_detached_houses >= 20000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount invested in condos:", amount_invested_in_condos.value())
print("The amount invested in detached houses:", amount_invested_in_detached_houses.value())
print("The total profit from the investment:", objective.value())
print("## end solving")