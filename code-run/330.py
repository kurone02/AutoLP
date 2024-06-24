from pulp import *

# Define the decision variables
# number of medication patches
num_medication_patches = LpVariable("MedicationPatches", lowBound=0, cat='Integer')
# number of anti-biotic creams
num_antibiotic_creams = LpVariable("AntibioticCreams", lowBound=0, cat='Integer') 

# Define the question as a minimum or maximum problem
problem = LpProblem("HospitalProblem", LpMaximize)

# Define the objective function
# maximize the total number of people that can be treated
objective = 3 * num_medication_patches + 2 * num_antibiotic_creams
problem += objective

# Define the constraints
# total number of batches
problem += num_medication_patches + num_antibiotic_creams <= 100
# total preparation time
problem += 3 * num_medication_patches + 5 * num_antibiotic_creams <= 400
# total material units
problem += 5 * num_medication_patches + 6 * num_antibiotic_creams <= 530
# at least twice as many anti-biotic creams as medication patches
problem += num_antibiotic_creams >= 2 * num_medication_patches

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Output the answer
print("## start solving")
print("The number of medication patches:", num_medication_patches.value())
print("The number of anti-biotic creams:", num_antibiotic_creams.value())
print("The number of people that can be treated:", objective.value())
print("## end solving")