from pulp import *

# Define the decision variables
# number of freight trips
num_freight_trips = LpVariable("NumFreightTrips", lowBound=5, cat='Integer')
# number of air trips
num_air_trips = LpVariable("NumAirTrips", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CandleMakingCompanyProblem", LpMinimize)

# Define the objective function
# minimize the total number of trips
objective = num_freight_trips + num_air_trips
problem += objective

# Define the constraints
# total tons of candles to be transported
problem += 5 * num_freight_trips + 3 * num_air_trips >= 200
# total cost of transport
problem += 300 * num_freight_trips + 550 * num_air_trips <= 20000
# at least 30% of tons of candles must be transported through air
problem += 3 * num_air_trips >= 0.3 * (5 * num_freight_trips + 3 * num_air_trips)
# at least 5 trips through freight
problem += num_freight_trips >= 5

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of freight trips:", num_freight_trips.value())
print("The number of air trips:", num_air_trips.value())
print("The total number of trips:", objective.value())
print("## end solving")