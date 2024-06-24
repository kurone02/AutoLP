from pulp import *

# Define the decision variables
# number of social media commercials
num_social_media = LpVariable("NumSocialMedia", lowBound=0, cat='Integer')
# number of television commercials
num_television = LpVariable("NumTelevision", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CosmeticsAdProblem", LpMinimize)

# Define the objective function
# minimize the total cost
objective = 30000 * num_social_media + 50000 * num_television
problem += objective

# Define the constraints
# minimum audience for young girls
problem += 5 * num_social_media + 3 * num_television >= 20000000
# minimum audience for middle-aged women
problem += num_social_media + 7 * num_television >= 30000000

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of social media commercials:", num_social_media.value())
print("The number of television commercials:", num_television.value())
print("The minimum cost:", objective.value())
print("## end solving")