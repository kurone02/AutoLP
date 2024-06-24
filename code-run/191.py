from pulp import *

# Define the variables
num_students_NC = LpVariable("NumStudentsNC", lowBound=0, cat='Integer')
num_students_NW = LpVariable("NumStudentsNW", lowBound=0, cat='Integer')
num_students_NS = LpVariable("NumStudentsNS", lowBound=0, cat='Integer')
num_students_EC = LpVariable("NumStudentsEC", lowBound=0, cat='Integer')
num_students_EW = LpVariable("NumStudentsEW", lowBound=0, cat='Integer')
num_students_ES = LpVariable("NumStudentsES", lowBound=0, cat='Integer')
num_students_CC = LpVariable("NumStudentsCC", lowBound=0, cat='Integer')
num_students_CW = LpVariable("NumStudentsCW", lowBound=0, cat='Integer')
num_students_CS = LpVariable("NumStudentsCS", lowBound=0, cat='Integer')
num_students_SC = LpVariable("NumStudentsSC", lowBound=0, cat='Integer')
num_students_SW = LpVariable("NumStudentsSW", lowBound=0, cat='Integer')
num_students_SS = LpVariable("NumStudentsSS", lowBound=0, cat='Integer')
num_students_WC = LpVariable("NumStudentsWC", lowBound=0, cat='Integer')
num_students_WW = LpVariable("NumStudentsWW", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("BusingMilesMinimization", LpMinimize)

# Define the objective function
problem += 8 * num_students_NC + 11 * num_students_NW + 14 * num_students_NS + 9 * num_students_EC + 16 * num_students_EW + 10 * num_students_ES + 8 * num_students_CW + 12 * num_students_CS + 12 * num_students_SW + 9 * num_students_SS + 8 * num_students_WC + 14 * num_students_EC + 11 * num_students_EW + 9 * num_students_ES + 12 * num_students_NS + 9 * num_students_EC + 16 * num_students_EW + 10 * num_students_ES

# Define the constraints
problem += num_students_NC + num_students_NW + num_students_NS <= 700
problem += num_students_EC + num_students_EW + num_students_ES <= 900
problem += num_students_CC + num_students_CW + num_students_CS <= 500
problem += num_students_SC + num_students_SW + num_students_SS <= 300
problem += num_students_WC + num_students_WW + num_students_WW <= 600
problem += num_students_NC <= 1200
problem += num_students_NW <= 1200
problem += num_students_NS <= 1200
problem += num_students_EC <= 1200
problem += num_students_EW <= 1200
problem += num_students_ES <= 1200
problem += num_students_CC <= 1200
problem += num_students_CW <= 1200
problem += num_students_CS <= 1200
problem += num_students_SC <= 1200
problem += num_students_SW <= 1200
problem += num_students_SS <= 1200
problem += num_students_WC <= 1200
problem += num_students_WW <= 1200

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of students from North to Central:", num_students_NC.value())
print("The number of students from North to West:", num_students_NW.value())
print("The number of students from North to South:", num_students_NS.value())
print("The number of students from East to Central:", num_students_EC.value())
print("The number of students from East to West:", num_students_EW.value())
print("The number of students from East to South:", num_students_ES.value())
print("The number of students from Central to Central:", num_students_CC.value())
print("The number of students from Central to West:", num_students_CW.value())
print("The number of students from Central to South:", num_students_CS.value())
print("The number of students from South to Central:", num_students_SC.value())
print("The number of students from South to West:", num_students_SW.value())
print("The number of students from South to South:", num_students_SS.value())
print("The number of students from West to Central:", num_students_WC.value())
print("The number of students from West to West:", num_students_WW.value())
print("Total busing miles traveled:", problem.objective.value())
print("## end solving")