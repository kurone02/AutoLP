from pulp import *

# Define the decision variables
# number of deliveries by cart
num_deliveries_by_cart = LpVariable("DeliveriesByCart", lowBound=0, cat='Integer')
# number of deliveries by hand
num_deliveries_by_hand = LpVariable("DeliveriesByHand", lowBound=3, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("DimSumRestaurantProblem", LpMinimize)

# Define the objective function
# minimize the total number of refills per hour
objective = (5 * num_deliveries_by_cart) + (20 * num_deliveries_by_hand)
problem += objective

# Define the constraints
# total number of customer interactions
problem += 70 * num_deliveries_by_cart + 85 * num_deliveries_by_hand >= 4000
# at least 70% of delivery shifts must be by cart
problem += num_deliveries_by_cart >= 0.7 * (num_deliveries_by_cart + num_deliveries_by_hand)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of deliveries by cart:", num_deliveries_by_cart.value())
print("The number of deliveries by hand:", num_deliveries_by_hand.value())
print("The total number of refills per hour:", objective.value())
print("## end solving")