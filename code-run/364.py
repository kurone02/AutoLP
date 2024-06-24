from pulp import *

# Define the decision variables
num_television = LpVariable("NumTVCommercials", lowBound=0, cat='Integer')
num_radio = LpVariable("NumRadioCommercials", lowBound=0, cat='Integer')
num_newspaper = LpVariable("NumNewspaperAds", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("AdvertisingExposureProblem", LpMaximize)

# Define the objective function
exposure = 20000 * num_television + 2000 * num_radio + 9000 * num_newspaper
problem += exposure

# Define the constraints
problem += 15000 * num_television + 6000 * num_radio + 4000 * num_newspaper <= 100000
problem += num_television <= 4
problem += num_radio <= 10
problem += num_newspaper <= 7
problem += num_television + num_radio + num_newspaper <= 15

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of television commercials:", num_television.value())
print("The number of radio commercials:", num_radio.value())
print("The number of newspaper ads:", num_newspaper.value())
print("The maximum exposure:", exposure.value())
print("## end solving")