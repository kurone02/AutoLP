from pulp import *

# Define the decision variables
# number of radio ads
num_radio_ads = LpVariable("NumRadioAds", lowBound=15, upBound=40, cat='Integer')
# number of social media ads
num_social_media_ads = LpVariable("NumSocialMediaAds", lowBound=35, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("CleaningCompanyAdvertisingProblem", LpMaximize)

# Define the objective function
# maximize the total viewers reached
objective = 60500 * num_radio_ads + 50000 * num_social_media_ads
problem += objective

# Define the constraints
# total advertising budget
problem += 5000 * num_radio_ads + 9150 * num_social_media_ads <= 900000
# radio ads constraint
problem += 15 <= num_radio_ads <= 40
# social media ads constraint
problem += num_social_media_ads >= 35

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of radio ads:", num_radio_ads.value())
print("The number of social media ads:", num_social_media_ads.value())
print("The total viewers reached:", objective.value())
print("## end solving")