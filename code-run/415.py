from pulp import *

# Define the decision variables
pounds_oats = LpVariable("PoundsOats", lowBound=0, cat='Continuous')
pounds_corn = LpVariable("PoundsCorn", lowBound=0, cat='Continuous')
pounds_soybeans = LpVariable("PoundsSoybeans", lowBound=0, cat='Continuous')
pounds_vitamin = LpVariable("PoundsVitamin", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("SouthforkFeedProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 0.50 * pounds_oats + 1.20 * pounds_corn + 0.60 * pounds_soybeans + 2.00 * pounds_vitamin
problem += objective

# Define the constraints
# At least 30% of the mix must be soybeans
problem += pounds_soybeans >= 0.30 * (pounds_oats + pounds_corn + pounds_vitamin)
# At least 20% of the mix must be the vitamin supplement
problem += pounds_vitamin >= 0.20 * (pounds_oats + pounds_corn + pounds_soybeans)
# The ratio of corn to oats cannot exceed 2 to 1
problem += pounds_corn <= 2 * pounds_oats
# The amount of oats cannot exceed the amount of soybeans
problem += pounds_oats <= pounds_soybeans
# The mix must weigh at least 500 pounds
problem += pounds_oats + pounds_corn + pounds_soybeans + pounds_vitamin >= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of pounds of oats:", value(pounds_oats))
print("The number of pounds of corn:", value(pounds_corn))
print("The number of pounds of soybeans:", value(pounds_soybeans))
print("The number of pounds of vitamin supplement:", value(pounds_vitamin))
print("The total cost of the mix:", value(objective))
print("## end solving")