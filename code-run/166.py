from pulp import *

# Define the decision variables
# course variables
courses = {
    "Calculus": LpVariable("Calculus", cat='Binary'),
    "Operations Research": LpVariable("Operations Research", cat='Binary'),
    "Data Structures": LpVariable("Data Structures", cat='Binary'),
    "Business Statistics": LpVariable("Business Statistics", cat='Binary'),
    "Computer Simulation": LpVariable("Computer Simulation", cat='Binary'),
    "Introduction to Computer Programming": LpVariable("Introduction to Computer Programming", cat='Binary'),
    "Forecasting": LpVariable("Forecasting", cat='Binary')
}

# Define the question as a minimum or maximum problem
problem = LpProblem("CourseSelection", LpMinimize)

# Define the objective function
# minimize the total number of courses
problem += lpSum(courses.values())

# Define the constraints
# at least two math courses
problem += courses["Calculus"] + courses["Operations Research"] + courses["Data Structures"] + courses["Business Statistics"] + courses["Forecasting"] >= 2
# at least two OR courses
problem += courses["Calculus"] + courses["Operations Research"] + courses["Computer Simulation"] + courses["Forecasting"] >= 2
# at least two computer courses
problem += courses["Data Structures"] + courses["Computer Simulation"] + courses["Introduction to Computer Programming"] >= 2
# prerequisite constraints
problem += courses["Introduction to Computer Programming"] <= courses["Computer Simulation"]
problem += courses["Introduction to Computer Programming"] <= courses["Data Structures"]
problem += courses["Business Statistics"] <= courses["Forecasting"]

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Calculus:", courses["Calculus"].value())
print("Operations Research:", courses["Operations Research"].value())
print("Data Structures:", courses["Data Structures"].value())
print("Business Statistics:", courses["Business Statistics"].value())
print("Computer Simulation:", courses["Computer Simulation"].value())
print("Introduction to Computer Programming:", courses["Introduction to Computer Programming"].value())
print("Forecasting:", courses["Forecasting"].value())
print("The minimum number of courses needed:", value(problem.objective))
print("## end solving")