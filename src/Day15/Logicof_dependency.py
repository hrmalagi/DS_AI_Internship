print("INDEPENDENT EVENTS")
print("-------------------")

p_heads = 1/2
p_six = 1/6
p_independent = p_heads * p_six
print("Probability of Heads AND 6 =", p_independent)

print("\nDEPENDENT EVENTS")
print("----------------")
# Total marbles = 10 (5 Red + 5 Blue)

# First red
p_first_red = 5/10

# After removing one red:
# Remaining red = 4
# Remaining total = 9
p_second_red = 4/9

# Multiply using conditional probability
p_dependent = p_first_red * p_second_red

print("Probability both marbles are Red =", p_dependent)

print("\nWhy denominator changed?")
print("Because we did NOT replace the first marble.")
print("Total marbles reduced from 10 to 9.")