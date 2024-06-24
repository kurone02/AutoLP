from pulp import *

# Define the decision variables
warehouse_NY = LpVariable("WarehouseNY", cat='Binary')
warehouse_LA = LpVariable("WarehouseLA", cat='Binary')
warehouse_Chicago = LpVariable("WarehouseChicago", cat='Binary')
warehouse_Atlanta = LpVariable("WarehouseAtlanta", cat='Binary')
units_NY_R1 = LpVariable("UnitsNYR1", lowBound=0, cat='Integer')
units_NY_R2 = LpVariable("UnitsNYR2", lowBound=0, cat='Integer')
units_NY_R3 = LpVariable("UnitsNYR3", lowBound=0, cat='Integer')
units_LA_R1 = LpVariable("UnitsLAR1", lowBound=0, cat='Integer')
units_LA_R2 = LpVariable("UnitsLAR2", lowBound=0, cat='Integer')
units_LA_R3 = LpVariable("UnitsLAR3", lowBound=0, cat='Integer')
units_Chicago_R1 = LpVariable("UnitsChicagoR1", lowBound=0, cat='Integer')
units_Chicago_R2 = LpVariable("UnitsChicagoR2", lowBound=0, cat='Integer')
units_Chicago_R3 = LpVariable("UnitsChicagoR3", lowBound=0, cat='Integer')
units_Atlanta_R1 = LpVariable("UnitsAtlantaR1", lowBound=0, cat='Integer')
units_Atlanta_R2 = LpVariable("UnitsAtlantaR2", lowBound=0, cat='Integer')
units_Atlanta_R3 = LpVariable("UnitsAtlantaR3", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("WarehouseProblem", LpMinimize)

# Define the objective function
problem += 400 * warehouse_NY + 500 * warehouse_LA + 300 * warehouse_Chicago + 150 * warehouse_Atlanta

# Define the constraints
problem += units_NY_R1 + units_NY_R2 + units_NY_R3 == 80 * warehouse_NY
problem += units_NY_R1 + units_NY_R2 + units_NY_R3 == 70 * warehouse_NY
problem += units_NY_R1 + units_NY_R2 + units_NY_R3 == 40 * warehouse_NY
problem += units_LA_R1 + units_LA_R2 + units_LA_R3 == 80 * warehouse_LA
problem += units_LA_R1 + units_LA_R2 + units_LA_R3 == 70 * warehouse_LA
problem += units_LA_R1 + units_LA_R2 + units_LA_R3 == 40 * warehouse_LA
problem += units_Chicago_R1 + units_Chicago_R2 + units_Chicago_R3 == 80 * warehouse_Chicago
problem += units_Chicago_R1 + units_Chicago_R2 + units_Chicago_R3 == 70 * warehouse_Chicago
problem += units_Chicago_R1 + units_Chicago_R2 + units_Chicago_R3 == 40 * warehouse_Chicago
problem += units_Atlanta_R1 + units_Atlanta_R2 + units_Atlanta_R3 == 80 * warehouse_Atlanta
problem += units_Atlanta_R1 + units_Atlanta_R2 + units_Atlanta_R3 == 70 * warehouse_Atlanta
problem += units_Atlanta_R1 + units_Atlanta_R2 + units_Atlanta_R3 == 40 * warehouse_Atlanta
problem += warehouse_NY + warehouse_LA + warehouse_Chicago + warehouse_Atlanta <= 2
problem += warehouse_Atlanta + warehouse_LA >= 1
problem += warehouse_NY - warehouse_LA <= 0

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The weekly cost of meeting demand is:", value(problem.objective))
print("Open New York Warehouse:", warehouse_NY.value())
print("Open Los Angeles Warehouse:", warehouse_LA.value())
print("Open Chicago Warehouse:", warehouse_Chicago.value())
print("Open Atlanta Warehouse:", warehouse_Atlanta.value())
print("Units from New York to Region 1:", units_NY_R1.value())
print("Units from New York to Region 2:", units_NY_R2.value())
print("Units from New York to Region 3:", units_NY_R3.value())
print("Units from Los Angeles to Region 1:", units_LA_R1.value())
print("Units from Los Angeles to Region 2:", units_LA_R2.value())
print("Units from Los Angeles to Region 3:", units_LA_R3.value())
print("Units from Chicago to Region 1:", units_Chicago_R1.value())
print("Units from Chicago to Region 2:", units_Chicago_R2.value())
print("Units from Chicago to Region 3:", units_Chicago_R3.value())
print("Units from Atlanta to Region 1:", units_Atlanta_R1.value())
print("Units from Atlanta to Region 2:", units_Atlanta_R2.value())
print("Units from Atlanta to Region 3:", units_Atlanta_R3.value())
print("## end solving")