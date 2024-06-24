from pulp import *

# Define the decision variables
bet_basketball = LpVariable("BetBasketball", lowBound=0, cat='Continuous')
bet_horse = LpVariable("BetHorse", lowBound=0, cat='Continuous')
bet_soccer = LpVariable("BetSoccer", lowBound=0, cat='Continuous')

# Define the question as a minimum or maximum problem
problem = LpProblem("GamblingProblem", LpMaximize)

# Define the objective function
objective = (1.2 * bet_basketball + 0.5 * bet_horse + 0.1 * bet_soccer) / (bet_basketball + bet_horse + bet_soccer)
problem += objective

# Define the constraints
problem += bet_basketball + bet_horse + bet_soccer <= 100000
problem += 0.5 * bet_basketball + 0.25 * bet_horse + 0.1 * bet_soccer <= 0.3 * (bet_basketball + bet_horse + bet_soccer)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The money to put on the basketball tournament:", bet_basketball.value())
print("The money to put on the horse race:", bet_horse.value())
print("The money to put on the soccer game:", bet_soccer.value())
print("The expected average payout:", objective.value())
print("## end solving")