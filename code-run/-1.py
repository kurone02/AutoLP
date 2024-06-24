from pulp import *

# Define the decision variables
# money to put on basketball tournament
money_basketball = LpVariable("MoneyBasketball", lowBound=0, cat='Continuous')
# money to put on horse race
money_horse_race = LpVariable("MoneyHorseRace", lowBound=0, cat='Continuous')
# money to put on soccer game
money_soccer = LpVariable("MoneySoccer", lowBound=0, cat='Continuous') 

# Define the question as a minimum or maximum problem
problem = LpProblem("GambleProblem", LpMaximize)

# Define the objective function
# maximize the expected average payout
objective = (1.2 * money_basketball + 0.5 * money_horse_race + 0.1 * money_soccer) / (money_basketball + money_horse_race + money_soccer)
problem += objective

# Define the constraints
# total money
problem += money_basketball + money_horse_race + money_soccer == 100000
# average chance of losing money
problem  += 0.5*money_basketball + 0.25*money_horse_race + 0.1*money_soccer <= 0.3*money_basketball + 0.3*money_horse_race + 0.3*money_soccer # problem += (0.5 * money_basketball + 0.25 * money_horse_race + 0.1 * money_soccer) / (money_basketball + money_horse_race + money_soccer) <= 0.3

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The money to put on the basketball tournament:", money_basketball.value())
print("The money to put on the horse race:", money_horse_race.value())
print("The money to put on the soccer game:", money_soccer.value())
print("The expected average payout:", objective.value())
print("## end solving")