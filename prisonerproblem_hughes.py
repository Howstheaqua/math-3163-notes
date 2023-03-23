#Author: Evan Hughes
import random

# Define numbers for the simulation
trials = 100000
successes = 0
prisoners = 500 # n
drawersOpened = 250 # k

# Make a set of drawers each one with the number of a prisoner
drawers = []
for i in range(prisoners):
    drawers.append(i)

def shuffleDrawers(drawers):
    random.shuffle(drawers)
    return drawers
random.shuffle(drawers) # randomize the drawers

# Check if a prisoner is in the first cycle of drawers
# Returns true if the prisoner will find their number following the best strategy
# Returns false if the prisoner opens the given amount of drawers without finding their number
def checkCycle(prisoner, drawers):
    next_box = prisoner
    for i in range(drawersOpened): # Check the first k drawers
        if prisoner == drawers[next_box]: # If the prisoner finds their number, they will succeed
            return True
        next_box = drawers[next_box] # If the prisoner doesn't find their number, move on to the next drawer using the number in the drawer
    return False
    

# Run the simulation
for i in range(trials):
    drawers = shuffleDrawers(drawers)
    success = True # Assume the group will succeed
    for prisoner_number in range(prisoners): 
        if checkCycle(prisoner_number, drawers) == False: 
            success = False # If one prisoner fails, the whole group fails
            break # To save time, if one prisoner fails, the whole group fails and move on to the next trial
    if success == True:
        successes += 1

# Print the results
print("Trials: " + str(trials))
print("Successes: " + str(successes))
print("Relative frequency of successes: " + str(successes/trials))
            


