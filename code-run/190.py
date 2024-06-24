from pulp import *

# Define the months
months = ['January', 'February', 'March', 'April', 'May', 'June']
demands = {'January': 370, 'February': 430, 'March': 380, 'April': 450, 'May': 520, 'June': 440}

# Define the decision variables
variables = LpVariable.dicts("Production", (months, ['Regular', 'Overtime', 'Inventory']), lowBound=0, cat='Integer')

# Define the problem
problem = LpProblem("ProductionPlanning", LpMinimize)

# Define the objective function
problem += lpSum([40 * variables[month]['Regular'] + 45 * variables[month]['Overtime'] + 3 * variables[month]['Inventory'] for month in months])

# Define the constraints
for month in months:
    # Monthly demand
    if month == 'January':
        problem += variables[month]['Regular'] + variables[month]['Overtime'] - variables[month]['Inventory'] == demands[month] + 10
    else:
        problem += variables[month]['Regular'] + variables[month]['Overtime'] - variables[month]['Inventory'] == demands[month] + variables[months[months.index(month)-1]]['Inventory']
    # Regular-time production capacity
    problem += variables[month]['Regular'] <= 420
    # Overtime production capacity
    problem += variables[month]['Overtime'] <= 80

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
for month in months:
    print("Month {} Regular-time production: {}".format(month, variables[month]['Regular'].value()))
    print("Month {} Overtime production: {}".format(month, variables[month]['Overtime'].value()))
    print("Month {} Inventory at the end of the month: {}".format(month, variables[month]['Inventory'].value()))
print("Total cost: {}".format(problem.objective.value()))
print("## end solving")