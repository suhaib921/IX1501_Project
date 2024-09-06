import numpy as np

# Define the number of trials for the Monte Carlo simulation
num_trials = 1000

# Define the number of sides for each die (Platonic solids)
tetrahedron_sides = 4     # 4-sided die (Tetrahedron)
cube_sides = 6            # 6-sided die (Cube)
octahedron_sides = 8      # 8-sided die (Octahedron)
dodecahedron_sides = 12   # 12-sided die (Dodecahedron)
icosahedron_sides = 20    # 20-sided die (Icosahedron)

# Initialize a counter for the number of wins
wins = 0

# Monte Carlo simulation: perform 'num_trials' trials
for _ in range(num_trials):
    # Simulate rolling each die by generating a random number for each die
    roll_tetrahedron = np.random.randint(1, tetrahedron_sides + 1)
    roll_cube = np.random.randint(1, cube_sides + 1)
    roll_octahedron = np.random.randint(1, octahedron_sides + 1)
    roll_dodecahedron = np.random.randint(1, dodecahedron_sides + 1)
    roll_icosahedron = np.random.randint(1, icosahedron_sides + 1)
    
    # Calculate the sum of the five dice
    dice_sum = (roll_tetrahedron + roll_cube + roll_octahedron +
                roll_dodecahedron + roll_icosahedron)
    
    # Check if the sum meets the winning condition (S <= 10 or S >= 45)
    if dice_sum <= 10 or dice_sum >= 45:
        wins += 1  # Increment the win counter

# Estimate the probability of winning
winning_probability = wins / num_trials

# Output the result
print(f"Estimated probability of winning after {num_trials} trials: {winning_probability:.5f}")
