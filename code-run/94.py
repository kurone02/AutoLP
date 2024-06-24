from pulp import *

# Define the variables
kgs_feed_A = LpVariable("KgsFeedA", lowBound=0, cat='Continuous')
kgs_feed_B = LpVariable("KgsFeedB", lowBound=0, cat='Continuous')

# Define the problem
problem = LpProblem("FarmerFeedMixProblem", LpMinimize)
objective = 100 * kgs_feed_A + 80 * kgs_feed_B
problem += objective

# Define the constraints
problem += 10 * kgs_feed_A + 7 * kgs_feed_B >= 30
problem += 8 * kgs_feed_A + 15 * kgs_feed_B >= 50

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The kilograms of Feed A in the mixture:", value(kgs_feed_A))
print("The kilograms of Feed B in the mixture:", value(kgs_feed_B))
print("The minimum cost of the mixture:", value(objective))
print("## end solving")