from pulp import *

# Define the decision variables
# number of television commercials
num_tv_commercials = LpVariable("NumTVCommercials", lowBound=0, cat='Integer')
# number of radio commercials
num_radio_commercials = LpVariable("NumRadioCommercials", lowBound=0, cat='Integer') 
# number of newspaper ads
num_newspaper_ads = LpVariable("NumNewspaperAds", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("AdDeliveryProblem", LpMaximize)

# Define the objective function
# maximize the total exposure
objective = 20000 * num_tv_commercials + 6000 * num_radio_commercials + 4000 * num_newspaper_ads
problem += objective

# Define the constraints
# total cost
problem += 15000 * num_tv_commercials + 6000 * num_radio_commercials + 4000 * num_newspaper_ads <= 100000
# total television time
problem += num_tv_commercials <= 4
# total radio time
problem += num_radio_commercials <= 10
# total newspaper space
problem += num_newspaper_ads <= 7
# total number of commercials and/or ads
problem += num_tv_commercials + num_radio_commercials + num_newspaper_ads <= 15

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of television commercials:", num_tv_commercials.value())
print("The number of radio commercials:", num_radio_commercials.value())
print("The number of newspaper ads:", num_newspaper_ads.value())
print("The maximum exposure:", objective.value())
print("## end solving")