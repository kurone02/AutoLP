from pulp import *

# Define the decision variables
open_NY = LpVariable("OpenNY", cat='Binary')
open_LA = LpVariable("OpenLA", cat='Binary')
open_Chi = LpVariable("OpenChi", cat='Binary')
open_Atl = LpVariable("OpenAtl", cat='Binary')
units_NY_R1 = LpVariable("UnitsNYR1", lowBound=0, cat='Integer')
units_NY_R2 = LpVariable("UnitsNYR2", lowBound=0, cat='Integer')
units_NY_R3 = LpVariable("UnitsNYR3", lowBound=0, cat='Integer')
units_LA_R1 = LpVariable("UnitsLAR1", lowBound=0, cat='Integer')
units_LA_R2 = LpVariable("UnitsLAR2", lowBound=0, cat='Integer')
units_LA_R3 = LpVariable("UnitsLAR3", lowBound=0, cat='Integer')
units_Chi_R1 = LpVariable("UnitsChiR1", lowBound=0, cat='Integer')
units_Chi_R2 = LpVariable("UnitsChiR2", lowBound=0, cat='Integer')
units_Chi_R3 = LpVariable("UnitsChiR3", lowBound=0, cat='Integer')
units_Atl_R1 = LpVariable("UnitsAtlR1", lowBound=0, cat='Integer')
units_Atl_R2 = LpVariable("UnitsAtlR2", lowBound=0, cat='Integer')
units_Atl_R3 = LpVariable("UnitsAtlR3", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("WarehouseProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 400 * open_NY + 500 * open_LA + 300 * open_Chi + 150 * open_Atl
problem += objective

# Define the constraints
# meet weekly demands
problem += units_NY_R1 + units_NY_R2 + units_NY_R3 + units_LA_R1 + units_LA_R2 + units_LA_R3 + units_Chi_R1 + units_Chi_R2 + units_Chi_R3 + units_Atl_R1 + units_Atl_R2 + units_Atl_R3 >= 220
# if New York is opened, then Los Angeles is opened
problem += open_LA >= open_NY
# at most two warehouses can be opened
problem += open_NY + open_LA + open_Chi + open_Atl <= 2
# either Atlanta or Los Angeles is opened
problem += open_LA + open_Atl >= 1

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The weekly cost of meeting demand is:", value(objective))
print("Open New York Warehouse:", open_NY.value())
print("Open Los Angeles Warehouse:", open_LA.value())
print("Open Chicago Warehouse:", open_Chi.value())
print("Open Atlanta Warehouse:", open_Atl.value())
print("Units from New York to Region 1:", units_NY_R1.value())
print("Units from New York to Region 2:", units_NY_R2.value())
print("Units from New York to Region 3:", units_NY_R3.value())
print("Units from Los Angeles to Region 1:", units_LA_R1.value())
print("Units from Los Angeles to Region 2:", units_LA_R2.value())
print("Units from Los Angeles to Region 3:", units_LA_R3.value())
print("Units from Chicago to Region 1:", units_Chi_R1.value())
print("Units from Chicago to Region 2:", units_Chi_R2.value())
print("Units from Chicago to Region 3:", units_Chi_R3.value())
print("Units from Atlanta to Region 1:", units_Atl_R1.value())
print("Units from Atlanta to Region 2:", units_Atl_R2.value())
print("Units from Atlanta to Region 3:", units_Atl_R3.value())
print("## end solving")