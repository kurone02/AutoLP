from pulp import *

# Define the decision variables
num_regular_mix = LpVariable("NumRegularMix", lowBound=0, cat='Integer')
num_deluxe_mix = LpVariable("NumDeluxeMix", lowBound=0, cat='Integer')
num_cashew_boxes = LpVariable("NumCashewBoxes", lowBound=0, cat='Integer')
num_raisin_boxes = LpVariable("NumRaisinBoxes", lowBound=0, cat='Integer')
num_caramel_boxes = LpVariable("NumCaramelBoxes", lowBound=0, cat='Integer')
num_chocolate_boxes = LpVariable("NumChocolateBoxes", lowBound=0, cat='Integer')

# Define the question as a minimum or maximum problem
problem = LpProblem("CandyCounterProblem", LpMaximize)

# Define the objective function
# maximize the total profit
objective = 0.8 * num_regular_mix + 0.9 * num_deluxe_mix + 0.7 * num_cashew_boxes + 0.6 * num_raisin_boxes + 0.5 * num_caramel_boxes + 0.75 * num_chocolate_boxes
problem += objective

# Define the constraints
# capacity constraint for cashews
problem += num_regular_mix + 0.5 * num_deluxe_mix + num_cashew_boxes <= 120
# capacity constraint for raisins
problem += num_raisin_boxes <= 200
# capacity constraint for caramels
problem += num_caramel_boxes <= 100
# capacity constraint for chocolates
problem += num_regular_mix + 0.5 * num_deluxe_mix + num_chocolate_boxes <= 160
# minimum boxes for cashews
problem += num_cashew_boxes >= 20
# minimum boxes for raisins
problem += num_raisin_boxes >= 20
# minimum boxes for caramels
problem += num_caramel_boxes >= 20
# minimum boxes for chocolates
problem += num_chocolate_boxes >= 20

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of regular mix boxes:", num_regular_mix.value())
print("The number of deluxe mix boxes:", num_deluxe_mix.value())
print("The number of cashew boxes:", num_cashew_boxes.value())
print("The number of raisin boxes:", num_raisin_boxes.value())
print("The number of caramel boxes:", num_caramel_boxes.value())
print("The number of chocolate boxes:", num_chocolate_boxes.value())
print("The maximum profit:", objective.value())
print("## end solving")