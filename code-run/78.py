from pulp import *

# Define the variables
num_vehicle_tickets = LpVariable("NumVehicleTickets", lowBound=10, cat='Integer')
num_passenger_tickets = LpVariable("NumPassengerTickets", lowBound=0, cat='Integer') 

# Define the problem as a maximum problem
problem = LpProblem("FerryTicketsProblem", LpMaximize)

# Define the objective function
objective = 50 * num_vehicle_tickets + 50 * num_passenger_tickets
problem += objective

# Define the constraints
problem += num_vehicle_tickets + num_passenger_tickets <= 100
problem += num_passenger_tickets >= 5 * num_vehicle_tickets

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of vehicle tickets sold:", num_vehicle_tickets.value())
print("The number of passenger tickets sold:", num_passenger_tickets.value())
print("Total profit:", objective.value())
print("## end solving")