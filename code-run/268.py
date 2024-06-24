from pulp import *

# Define the decision variables
# amount of light oil
amount_light_oil = LpVariable("AmountLightOil", lowBound=0, cat='Continuous')
# amount of non-sticky oil
amount_non_sticky_oil = LpVariable("AmountNonStickyOil", lowBound=0, cat='Continuous')
# amount of heavy oil
amount_heavy_oil = LpVariable("AmountHeavyOil", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("OilProcessingProblem", LpMaximize)

# Define the objective function
# maximize the total net revenue
objective = 550 * amount_light_oil + 750 * amount_non_sticky_oil + 950 * amount_heavy_oil
problem += objective

# Define the constraints
# compound A constraint
problem += 3 * amount_light_oil + 6 * amount_non_sticky_oil + 9 * amount_heavy_oil <= 250
# compound B constraint
problem += 3 * amount_light_oil + 2 * amount_non_sticky_oil + 3 * amount_heavy_oil <= 150

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The amount of light oil:", value(amount_light_oil))
print("The amount of non-sticky oil:", value(amount_non_sticky_oil))
print("The amount of heavy oil:", value(amount_heavy_oil))
print("The net revenue is:", value(objective))
print("## end solving")