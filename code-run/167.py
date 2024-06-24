from pulp import *

# Define the decision variables
# Whether to take the math course or not
Math = LpVariable("Math", lowBound=0, upBound=1, cat='Integer')
# Whether to take the OR course or not
OR = LpVariable("OR", lowBound=0, upBound=1, cat='Integer')
# Whether to take the Computer course or not
Computer = LpVariable("Computer", lowBound=0, upBound=1, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("CourseSchedulingProblem", LpMinimize)

# Define the objective function
# Minimize the total number of courses needed
problem += Math + OR + Computer

# Define the constraints
# Math requirement
problem += Math >= 2
# OR requirement
problem += OR >= 2
# Computer requirement
problem += Computer >= 2

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Calculus:", Math.value())
print("Operations Research:", OR.value())
print("Data Structures:", Computer.value())
print("Business Statistics:", Computer.value())
print("Computer Simulation:", Math.value())
print("Introduction to Computer Programming:", Math.value())
print("Forecasting:", OR.value())
print("The minimum number of courses needed:", value(problem.objective))
print("## end solving")