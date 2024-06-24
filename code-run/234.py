from pulp import *

# Define the decision variables
# number of small jars
num_small_jars = LpVariable("NumSmallJars", lowBound=0, cat='Integer')
# number of large jars
num_large_jars = LpVariable("NumLargeJars", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("JamShippingProblem", LpMinimize)

# Define the objective function
problem += num_small_jars + num_large_jars

# Define the constraints
# the total amount of jam to be shipped
problem += 50 * num_small_jars + 200 * num_large_jars >= 100000
# the number of large jars cannot exceed the number of small jars
problem += num_large_jars <= num_small_jars

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of small jars:", num_small_jars.value())
print("The number of large jars:", num_large_jars.value())
print("The total number of jars used:", (num_small_jars.value() + num_large_jars.value()))
print("## end solving")