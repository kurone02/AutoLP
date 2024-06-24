from pulp import *

# Define the decision variables
# square feet for phone production
phone_sq_feet = LpVariable("PhoneSqFeet", lowBound=0, cat='Integer')
# square feet for laptop production
laptop_sq_feet = LpVariable("LaptopSqFeet", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("FactoryLayoutProblem", LpMaximize)

# Define the objective function
# maximize the total net revenue
objective = 50 * phone_sq_feet + 70 * laptop_sq_feet
problem += objective

# Define the constraints
# total labor hours
problem += 2 * phone_sq_feet + 3 * laptop_sq_feet <= 2000
# total cost
problem += 12 * phone_sq_feet + 15 * laptop_sq_feet <= 5000
# total space
problem += phone_sq_feet + laptop_sq_feet <= 100

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The square feet for phone production:", phone_sq_feet.value())
print("The square feet for laptop production:", laptop_sq_feet.value())
print("The net revenue:", objective.value())
print("## end solving")