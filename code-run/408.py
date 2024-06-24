from pulp import *

# Define the variables
num_regular_month1 = LpVariable("NumRegularMonth1", lowBound=0, cat='Integer')
num_overtime_month1 = LpVariable("NumOvertimeMonth1", lowBound=0, cat='Integer')
inventory_month1 = LpVariable("InventoryMonth1", lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("BTDProblem", LpMinimize)

# Define the objective function
objective = 40 * num_regular_month1 + 45 * num_overtime_month1 + 3 * inventory_month1
problem += objective

# Define the constraints
problem += num_regular_month1 + num_overtime_month1 + inventory_month1 >= 370

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("Month 1 Regular-time production:", num_regular_month1.value())
print("Month 1 Overtime production:", num_overtime_month1.value())
print("Month 1 Inventory at the end of the month:", inventory_month1.value())
# Repeat the process for month 2, month 3, month 4, month 5, and month 6
print("Month 2 Regular-time production:", num_regular_month2.value())
print("Month 2 Overtime production:", num_overtime_month2.value())
print("Month 2 Inventory at the end of the month:", inventory_month2.value())
print("Month 3 Regular-time production:", num_regular_month3.value())
print("Month 3 Overtime production:", num_overtime_month3.value())
print("Month 3 Inventory at the end of the month:", inventory_month3.value())
print("Month 4 Regular-time production:", num_regular_month4.value())
print("Month 4 Overtime production:", num_overtime_month4.value())
print("Month 4 Inventory at the end of the month:", inventory_month4.value())
print("Month 5 Regular-time production:", num_regular_month5.value())
print("Month 5 Overtime production:", num_overtime_month5.value())
print("Month 5 Inventory at the end of the month:", inventory_month5.value())
print("Month 6 Regular-time production:", num_regular_month6.value())
print("Month 6 Overtime production:", num_overtime_month6.value())
print("Month 6 Inventory at the end of the month:", inventory_month6.value())
print("Total cost:", objective.value())
print("## end solving")