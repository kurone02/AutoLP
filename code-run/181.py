from pulp import *

# Define the decision variables
fire_station_city_1 = LpVariable("FireStationCity1", cat='Binary')
fire_station_city_2 = LpVariable("FireStationCity2", cat='Binary')
fire_station_city_3 = LpVariable("FireStationCity3", cat='Binary')
fire_station_city_4 = LpVariable("FireStationCity4", cat='Binary')
fire_station_city_5 = LpVariable("FireStationCity5", cat='Binary')
fire_station_city_6 = LpVariable("FireStationCity6", cat='Binary')

# Define the problem
problem = LpProblem("FireStationProblem", LpMinimize)

# Define the objective function
problem += fire_station_city_1 + fire_station_city_2 + fire_station_city_3 + fire_station_city_4 + fire_station_city_5 + fire_station_city_6

# Define the constraints
problem += [time_to_city_j - 15 * (1 - fire_station_city_j) <= 0 for time_to_city_j in [10, 25, 15, 15, 14]]
problem += [time_to_city_j - 15 * (1 - fire_station_city_j) <= 0 for time_to_city_j in [20, 35, 30, 25, 25]]
problem += [time_to_city_j - 15 * (1 - fire_station_city_j) <= 0 for time_to_city_j in [30, 20, 20, 15, 14]]
problem += [time_to_city_j - 15 * (1 - fire_station_city_j) <= 0 for time_to_city_j in [30, 10, 20, 25, 0]]
problem += [time_to_city_j - 15 * (1 - fire_station_city_j) <= 0 for time_to_city_j in [20, 10, 20, 20, 14]]
problem += [time_to_city_j - 15 * (1 - fire_station_city_j) <= 0 for time_to_city_j in [10, 0, 25, 25, 14]]

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The optimal number of fire stations to be built is:", value(problem.objective))
print("Whether a fire stations should be built in City 1:", fire_station_city_1.value())
print("Whether a fire stations should be built in City 2:", fire_station_city_2.value())
print("Whether a fire stations should be built in City 3:", fire_station_city_3.value())
print("Whether a fire stations should be built in City 4:", fire_station_city_4.value())
print("Whether a fire stations should be built in City 5:", fire_station_city_5.value())
print("Whether a fire stations should be built in City 6:", fire_station_city_6.value())
print("## end solving")