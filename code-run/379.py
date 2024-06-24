from pulp import *

# Define the problem
prob = LpProblem("WarehouseLocationProblem", LpMinimize)

# Define the decision variables
NY = LpVariable("NY", cat='Binary')
LA = LpVariable("LA", cat='Binary')
Chicago = LpVariable("Chicago", cat='Binary')
Atlanta = LpVariable("Atlanta", cat='Binary')

# Define the shipping variables
NY_R1 = LpVariable("NY_R1", lowBound=0, cat='Integer')
NY_R2 = LpVariable("NY_R2", lowBound=0, cat='Integer')
NY_R3 = LpVariable("NY_R3", lowBound=0, cat='Integer')
LA_R1 = LpVariable("LA_R1", lowBound=0, cat='Integer')
LA_R2 = LpVariable("LA_R2", lowBound=0, cat='Integer')
LA_R3 = LpVariable("LA_R3", lowBound=0, cat='Integer')
Chicago_R1 = LpVariable("Chicago_R1", lowBound=0, cat='Integer')
Chicago_R2 = LpVariable("Chicago_R2", lowBound=0, cat='Integer')
Chicago_R3 = LpVariable("Chicago_R3", lowBound=0, cat='Integer')
Atlanta_R1 = LpVariable("Atlanta_R1", lowBound=0, cat='Integer')
Atlanta_R2 = LpVariable("Atlanta_R2", lowBound=0, cat='Integer')
Atlanta_R3 = LpVariable("Atlanta_R3", lowBound=0, cat='Integer')

# Define the objective function
prob += 400*NY + 500*LA + 300*Chicago + 150*Atlanta

# Define the constraints
prob += NY <= LA  # If the New York warehouse is opened, then the Los Angeles warehouse must be opened
prob += NY + LA + Chicago + Atlanta <= 2  # At most two warehouses can be opened
prob += Atlanta + LA >= 1  # Either the Atlanta or the Los Angeles warehouse must be opened
prob += NY_R1 + NY_R2 + NY_R3 <= 100  # The total units shipped from New York must be less than or equal to 100
prob += LA_R1 + LA_R2 + LA_R3 <= 100  # The total units shipped from Los Angeles must be less than or equal to 100
prob += Chicago_R1 + Chicago_R2 + Chicago_R3 <= 100  # The total units shipped from Chicago must be less than or equal to 100
prob += Atlanta_R1 + Atlanta_R2 + Atlanta_R3 <= 100  # The total units shipped from Atlanta must be less than or equal to 100

# Solve the problem
prob.solve()

# Output the answer
print("## start solving")
print("The weekly cost of meeting demand is: ", value(prob.objective))
print("Open New York Warehouse: ", NY.varValue)
print("Open Los Angeles Warehouse: ", LA.varValue)
print("Open Chicago Warehouse: ", Chicago.varValue)
print("Open Atlanta Warehouse: ", Atlanta.varValue)
print("Units from New York to Region 1: ", NY_R1.varValue)
print("Units from New York to Region 2: ", NY_R2.varValue)
print("Units from New York to Region 3: ", NY_R3.varValue)
print("Units from Los Angeles to Region 1: ", LA_R1.varValue)
print("Units from Los Angeles to Region 2: ", LA_R2.varValue)
print("Units from Los Angeles to Region 3: ", LA_R3.varValue)
print("Units from Chicago to Region 1: ", Chicago_R1.varValue)
print("Units from Chicago to Region 2: ", Chicago_R2.varValue)
print("Units from Chicago to Region 3: ", Chicago_R3.varValue)
print("Units from Atlanta to Region 1: ", Atlanta_R1.varValue)
print("Units from Atlanta to Region 2: ", Atlanta_R2.varValue)
print("Units from Atlanta to Region 3: ", Atlanta_R3.varValue)
print("## end solving")