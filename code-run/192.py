from pulp import *

# Define the decision variables
paper_stock1 = LpVariable("PaperStock1", lowBound=0, cat='Integer')
paper_stock2 = LpVariable("PaperStock2", lowBound=0, cat='Integer')
paper_stock3 = LpVariable("PaperStock3", lowBound=0, cat='Integer')
paper_stock4 = LpVariable("PaperStock4", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("WesternPulpProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 150 * paper_stock1 + 110 * paper_stock2 + 90 * paper_stock3 + 50 * paper_stock4
problem += objective

# Define the constraints
# total strength
problem += 8 * paper_stock1 + 6 * paper_stock2 + 5 * paper_stock3 + 3 * paper_stock4 >= 7 * 500
# total color
problem += 9 * paper_stock1 + 7 * paper_stock2 + 5 * paper_stock3 + 4 * paper_stock4 >= 5 * 500
# total texture
problem += 8 * paper_stock1 + 5 * paper_stock2 + 6 * paper_stock3 + 5 * paper_stock4 >= 6 * 500
# total quantity
problem += paper_stock1 + paper_stock2 + paper_stock3 + paper_stock4 >= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The quantity of paper stock 1:", paper_stock1.value())
print("The quantity of paper stock 2:", paper_stock2.value())
print("The quantity of paper stock 3:", paper_stock3.value())
print("The quantity of paper stock 4:", paper_stock4.value())
print("The minimum cost:", objective.value())
print("## end solving")