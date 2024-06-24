from pulp import *

# define the problem
prob = LpProblem("CourseSelection", LpMinimize)

# define the variables
calculus = LpVariable("Calculus", cat='Binary')
operations_research = LpVariable("OperationsResearch", cat='Binary')
data_structures = LpVariable("DataStructures", cat='Binary')
business_statistics = LpVariable("BusinessStatistics", cat='Binary')
computer_simulation = LpVariable("ComputerSimulation", cat='Binary')
introduction_to_computer_programming = LpVariable("IntroductionToComputerProgramming", cat='Binary')
forecasting = LpVariable("Forecasting", cat='Binary')

# define the objective
prob += calculus + operations_research + data_structures + business_statistics + computer_simulation + introduction_to_computer_programming + forecasting

# define the constraints
prob += calculus + operations_research + business_statistics + forecasting >= 2
prob += operations_research + computer_simulation + forecasting >= 2
prob += data_structures + computer_simulation + introduction_to_computer_programming >= 2
prob += business_statistics - calculus >= 0
prob += introduction_to_computer_programming - data_structures >= 0
prob += forecasting - business_statistics >= 0

# solve the problem
status = prob.solve(PULP_CBC_CMD(msg=0))

# print the solution
print("## start solving")
print("Calculus:", calculus.varValue)
print("Operations Research:", operations_research.varValue)
print("Data Structures:", data_structures.varValue)
print("Business Statistics:", business_statistics.varValue)
print("Computer Simulation:", computer_simulation.varValue)
print("Introduction to Computer Programming:", introduction_to_computer_programming.varValue)
print("Forecasting:", forecasting.varValue)
print("The minimum number of courses needed:", value(prob.objective))
print("## end solving")