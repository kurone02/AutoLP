from pulp import *

# Define the decision variables
# number of glass jars
num_glass_jars = LpVariable("NumGlassJars", lowBound=20, cat='Integer')
# number of plastic jars
num_plastic_jars = LpVariable("NumPlasticJars", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HoneyFarmerJarProblem", LpMaximize)

# Define the objective function
# maximize the total number of jars filled
objective = num_glass_jars + num_plastic_jars
problem += objective

# Define the constraints
# total amount of honey
problem += 250 * num_glass_jars + 300 * num_plastic_jars <= 20000
# plastic jar constraint
problem += num_plastic_jars >= 2 * num_glass_jars
# glass jar constraint
problem += num_glass_jars >= 20

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of glass jars:", num_glass_jars.value())
print("The number of plastic jars:", num_plastic_jars.value())
print("The total number of jars filled:", objective.value())
print("## end solving")