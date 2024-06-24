from pulp import *

# Define the decision variables
# number of commercials on Pi TV
num_pi_tv = LpVariable("NumPiTV", lowBound=0, cat='Integer')
# number of commercials on Beta Video
num_beta_video = LpVariable("NumBetaVideo", lowBound=0, cat='Integer')
# number of commercials on Gamma Live
num_gamma_live = LpVariable("NumGammaLive", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("FoodCompanyProblem", LpMaximize)

# Define the objective function
problem += 2000 * num_pi_tv + 5000 * num_beta_video + 9000 * num_gamma_live

# Define the constraints
problem += 1200 * num_pi_tv + 2000 * num_beta_video + 4000 * num_gamma_live <= 20000
problem += num_beta_video <= 8
problem  += 3*num_gamma_live <= num_beta_video + num_gamma_live + num_pi_tv # problem += num_gamma_live <= 1/3 * (num_pi_tv + num_beta_video + num_gamma_live)
problem += num_pi_tv >= 0.2 * (num_pi_tv + num_beta_video + num_gamma_live)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of commercials on Pi TV:", value(num_pi_tv))
print("The number of commercials on Beta Video:", value(num_beta_video))
print("The number of commercials on Gamma Live:", value(num_gamma_live))
print("Total audience reached:", value(2000 * num_pi_tv + 5000 * num_beta_video + 9000 * num_gamma_live))
print("## end solving")