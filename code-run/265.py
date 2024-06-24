from pulp import *

# Define the decision variables
# number of reams of graph paper
num_graph_paper = LpVariable("NumGraphPaper", lowBound=0, cat='Integer')
# number of reams of music paper
num_music_paper = LpVariable("NumMusicPaper", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("ForestPaperProfitMaximization", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 4 * num_graph_paper + 2.5 * num_music_paper
problem += objective

# Define the constraints
# total time on the printing machine
problem += 3 * num_graph_paper + 1.5 * num_music_paper <= 350
# total time on the scanning machine
problem += 5.5 * num_graph_paper + 3 * num_music_paper <= 350

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of reams of graph paper:", num_graph_paper.value())
print("The number of reams of music paper:", num_music_paper.value())
print("The maximum profit:", objective.value())
print("## end solving")