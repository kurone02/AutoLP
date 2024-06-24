from pulp import *

# Define the decision variables
num_ztube_ads = LpVariable("NumZTubeAds", lowBound=0, cat='Integer')
num_soorchle_ads = LpVariable("NumSoorchleAds", lowBound=0, cat='Integer')
num_wassa_ads = LpVariable("NumWassaAds", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("AdvertisingProblem", LpMaximize)

# Define the objective function
# maximize the total audience
objective = 400000 * num_ztube_ads + 5000 * num_soorchle_ads + 3000 * num_wassa_ads
problem += objective

# Define the constraints
# total cost of ads
problem += 1000 * num_ztube_ads + 200 * num_soorchle_ads + 100 * num_wassa_ads <= 10000
# limit on soorchle ads
problem += num_soorchle_ads <= 15
# maximum proportion of ads on wassa
problem += num_wassa_ads <= num_ztube_ads + num_soorchle_ads
# minimum proportion of ads on z-tube
problem += num_ztube_ads >= 0.05 * (num_ztube_ads + num_soorchle_ads + num_wassa_ads)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of z-tube ads:", num_ztube_ads.value())
print("The number of soorchle ads:", num_soorchle_ads.value())
print("The number of wassa ads:", num_wassa_ads.value())
print("The total audience:", objective.value())
print("## end solving")