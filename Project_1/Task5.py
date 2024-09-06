import numpy as np
import matplotlib.pyplot as plt

# True probability of winning from Task 2 (this value may need to be adjusted based on Task 2 results)
P_true = 0.01068 # Approximate true probability of winning, adjust based on Task 2 if needed

# Function to simulate the dice rolls and estimate the probability of winning
def monte_carlo_simulation(num_trials):
    # Number of sides for each die (Platonic solids)
    tetrahedron_sides = 4     # 4-sided die (Tetrahedron)
    cube_sides = 6            # 6-sided die (Cube)
    octahedron_sides = 8      # 8-sided die (Octahedron)
    dodecahedron_sides = 12   # 12-sided die (Dodecahedron)
    icosahedron_sides = 20    # 20-sided die (Icosahedron)

    # Counter for the number of wins
    wins = 0

    # Monte Carlo simulation for 'num_trials' trials
    for _ in range(num_trials):
        # Roll each die (random number between 1 and the number of sides)
        roll_tetrahedron = np.random.randint(1, tetrahedron_sides + 1)
        roll_cube = np.random.randint(1, cube_sides + 1)
        roll_octahedron = np.random.randint(1, octahedron_sides + 1)
        roll_dodecahedron = np.random.randint(1, dodecahedron_sides + 1)
        roll_icosahedron = np.random.randint(1, icosahedron_sides + 1)

        # Calculate the sum of the five dice
        dice_sum = (roll_tetrahedron + roll_cube + roll_octahedron +
                    roll_dodecahedron + roll_icosahedron)

        # Check if the sum meets the winning condition (S ≤ 10 or S ≥ 45)
        if dice_sum <= 10 or dice_sum >= 45:
            wins += 1  # Increment the win counter

    # Estimated probability of winning
    return wins / num_trials

# Function to calculate the minimum number of trials needed for less than 10% relative error
def calculate_min_trials(P_true, relative_error_threshold):
    # Using the formula N > (1 - P_true) / (relative_error_threshold^2)
    return (1 - P_true) / (relative_error_threshold ** 2)

# Monte Carlo simulation for varying numbers of trials
trial_values = [10, 100, 1000, 10000, 100000]
estimated_probabilities = []

# Perform Monte Carlo simulation for each value of N (number of trials)
for N in trial_values:
    estimated_probability = monte_carlo_simulation(N)
    estimated_probabilities.append(estimated_probability)
    print(f"Estimated probability of winning after {N} trials: {estimated_probability:.5f}")

# Plot the estimated probabilities against the number of trials
plt.figure(figsize=(10, 6))
plt.plot(trial_values, estimated_probabilities, marker='o', linestyle='-', color='b', label='Estimated Probability')
plt.xscale('log')  # Logarithmic scale for the number of trials
plt.xlabel('Number of Trials (N)')
plt.ylabel('Estimated Probability of Winning')
plt.title('Convergence of Estimated Winning Probability with Increasing Trials')
plt.grid(True)
plt.legend()
plt.show()

# Calculate the minimum number of trials for less than 10% relative error
relative_error_threshold = 0.10
min_trials = calculate_min_trials(P_true, relative_error_threshold)

# Print the result
print(f"Minimum number of trials required for less than 10% relative error: {int(np.ceil(min_trials))}")
