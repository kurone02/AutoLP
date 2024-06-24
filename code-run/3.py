from pulp import *

# Define the decision variables
# number of soccer balls
num_soccer_balls = LpVariable("NumSoccerBalls", lowBound=0, cat='Integer')
# number of basket balls
num_basket_balls = LpVariable("NumBasketBalls", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("BallFactoryProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 4 * num_soccer_balls + 5 * num_basket_balls
problem += objective

# Define the constraints
# total time on the manufacturing machine
problem += 5 * num_soccer_balls + 7 * num_basket_balls <= 700
# total time for filling the balls with air
problem += 3 * num_soccer_balls + 4 * num_basket_balls <= 500

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of soccer balls:", num_soccer_balls.value())
print("The number of basket balls:", num_basket_balls.value())
print("The total profit:", objective.value())
print("## end solving")