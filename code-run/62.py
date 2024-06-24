from pulp import *

# Define the decision variables
num_ruby_cans = LpVariable("NumRubyCans", lowBound=0, cat='Integer')
num_sapphire_cans = LpVariable("NumSapphireCans", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("PaintStoreProblem", LpMinimize)

# Define the objective function
problem += 12 * num_ruby_cans + 15 * num_sapphire_cans

# Define the constraints
problem += 2 * num_ruby_cans + 4 * num_sapphire_cans >= 15
problem += 4 * num_ruby_cans + 6 * num_sapphire_cans >= 20
problem += 5 * num_ruby_cans + 2 * num_sapphire_cans >= 18

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of cans of Ruby paint:", num_ruby_cans.value())
print("The number of cans of Sapphire paint:", num_sapphire_cans.value())
print("The minimum cost of the mixture:", problem.objective.value())
print("## end solving")