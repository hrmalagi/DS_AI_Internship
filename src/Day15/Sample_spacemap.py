# Define actions
actions = ["Click", "Scroll", "Exit"]

sample_space = []
event = []

# Create all possible pairs
for first in actions:
    for second in actions:
        pair = (first, second)
        sample_space.append(pair)
        
        # Check if at least one Click
        if "Click" in pair:
            event.append(pair)

# Print results
print("Sample Space:", sample_space)
print("Event (At least one Click):", event)

probability = len(event) / len(sample_space)
print("Probability =", probability)

import random

count = 0
trials = 1000

for i in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 7:
        count += 1

probability = count / trials
print("Experimental Probability of Sum 7 =", probability)