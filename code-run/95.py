from pulp import *

# Define the decision variables
# number of thin jars
num_thin_jars = LpVariable("NumThinJars", lowBound=0, cat='Integer')
# number of stubby jars
num_stubby_jars = LpVariable("NumStubbyJars", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("TerracottaJarsProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 5 * num_thin_jars + 9 * num_stubby_jars
problem += objective

# Define the constraints
# total shaping time
problem += 50 * num_thin_jars + 30 * num_stubby_jars <= 3000
# total baking time
problem += 90 * num_thin_jars + 150 * num_stubby_jars <= 4000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of thin jars:", num_thin_jars.value())
print("The number of stubby jars:", num_stubby_jars.value())
print("The profit:", objective.value())
print("## end solving")